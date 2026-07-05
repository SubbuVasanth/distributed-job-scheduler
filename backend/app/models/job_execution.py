from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class JobExecution(Base):
    __tablename__ = "job_executions"

    id = Column(Integer, primary_key=True)

    job_id = Column(
        Integer,
        ForeignKey("jobs.id"),
        nullable=False,
    )

    worker_id = Column(
        Integer,
        ForeignKey("workers.id"),
        nullable=False,
    )

    attempt = Column(Integer, nullable=False)

    status = Column(String(30), nullable=False)

    error_message = Column(String(500))

    started_at = Column(DateTime, default=datetime.utcnow)

    finished_at = Column(DateTime)

    execution_time_ms = Column(Integer)

    job = relationship("Job")

    worker = relationship("Worker")