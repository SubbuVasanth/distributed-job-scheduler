from apscheduler.schedulers.background import BackgroundScheduler
from app.core.database import SessionLocal
from app.models.job import Job, JobStatus
from datetime import datetime

scheduler = BackgroundScheduler()

def transition_scheduled_jobs():
    db = SessionLocal()
    try:
        scheduled_jobs = (
            db.query(Job)
            .filter(
                Job.status == JobStatus.SCHEDULED,
                Job.available_at <= datetime.utcnow()
            )
            .all()
        )
        for job in scheduled_jobs:
            job.status = JobStatus.QUEUED
            print(f"Job {job.id} transitioned to QUEUED.")
        db.commit()
    finally:
        db.close()

def start_scheduler():
    scheduler.add_job(transition_scheduled_jobs, 'interval', seconds=10)
    scheduler.start()
    print("Scheduler Started and listening for scheduled jobs.")