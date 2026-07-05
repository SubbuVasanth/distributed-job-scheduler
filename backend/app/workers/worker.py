import time
from datetime import datetime

from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.job import Job, JobStatus


def process_jobs():

    print("Worker started...")

    while True:

        db: Session = SessionLocal()

        try:

            job = (
                db.query(Job)
                .filter(
                    Job.status == JobStatus.QUEUED,
                    Job.available_at <= datetime.utcnow()
                )
                .order_by(
                    Job.priority.desc(),
                    Job.created_at.asc()
                )
                .first()
            )

            if job:

                print(f"Processing Job {job.id}")

                job.status = JobStatus.CLAIMED

                db.commit()

                job.status = JobStatus.RUNNING

                db.commit()

                try:

                    time.sleep(3)

                    job.status = JobStatus.COMPLETED
                    job.completed_at = datetime.utcnow()

                except Exception:

                    job.attempt += 1

                    if job.attempt >= job.max_attempts:

                        job.status = JobStatus.DEAD

                    else:

                        job.status = JobStatus.QUEUED

                finally:

                    db.commit()

                print(f"Completed Job {job.id}")

            else:

                time.sleep(2)

        finally:

            db.close()


if __name__ == "__main__":
    process_jobs()