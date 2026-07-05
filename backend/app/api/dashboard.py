from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.job import Job, JobStatus
from app.models.queue import Queue

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def stats(db: Session = Depends(get_db)):

    return {
        "queued": db.query(Job).filter(Job.status == JobStatus.QUEUED).count(),
        "scheduled": db.query(Job).filter(Job.status == JobStatus.SCHEDULED).count(),
        "running": db.query(Job).filter(Job.status == JobStatus.RUNNING).count(),
        "completed": db.query(Job).filter(Job.status == JobStatus.COMPLETED).count(),
        "dead": db.query(Job).filter(Job.status == JobStatus.DEAD).count(),
        "queues": db.query(Queue).count(),
    }