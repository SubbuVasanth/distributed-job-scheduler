from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.job import Job, JobStatus
from app.models.queue import Queue
from app.models.project import Project
from app.models.user import User


class JobService:

    @staticmethod
    def create_job(
        db: Session,
        job_data,
        current_user: User
    ):

        queue = (
            db.query(Queue)
            .join(Project)
            .filter(
                Queue.id == job_data.queue_id,
                Project.owner_id == current_user.id
            )
            .first()
        )

        if queue is None:
            raise ValueError("Queue not found")

        available_at = datetime.utcnow()

        status = JobStatus.QUEUED

        if job_data.delay_seconds:

            available_at = (
                datetime.utcnow() +
                timedelta(seconds=job_data.delay_seconds)
            )

            status = JobStatus.SCHEDULED

        if job_data.scheduled_at:

            available_at = job_data.scheduled_at

            status = JobStatus.SCHEDULED

        job = Job(
            queue_id=job_data.queue_id,

            payload=job_data.payload,

            priority=job_data.priority,

            status=status,

            available_at=available_at,

            scheduled_at=job_data.scheduled_at,

            cron_expression=job_data.cron_expression,
        )

        db.add(job)

        db.commit()

        db.refresh(job)

        return job

    @staticmethod
    def get_jobs(
        db: Session,
        current_user: User
    ):

        return (
            db.query(Job)
            .join(Queue)
            .join(Project)
            .filter(Project.owner_id == current_user.id)
            .all()
        )

    @staticmethod
    def get_job(
        db: Session,
        job_id: int,
        current_user: User
    ):

        return (
            db.query(Job)
            .join(Queue)
            .join(Project)
            .filter(
                Job.id == job_id,
                Project.owner_id == current_user.id
            )
            .first()
        )

    @staticmethod
    def retry_job(
        db: Session,
        job_id: int,
        current_user: User
    ):
        job = JobService.get_job(db, job_id, current_user)
        if not job:
            return None
        
        job.status = JobStatus.QUEUED
        job.attempt = 0
        job.worker_id = None
        db.commit()
        db.refresh(job)
        return job