from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Column,
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    Integer,
    JSON,
    String,
)

from sqlalchemy.orm import relationship

from app.models.base import Base


class JobStatus(str, Enum):
    QUEUED = "QUEUED"
    SCHEDULED = "SCHEDULED"
    CLAIMED = "CLAIMED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    DEAD = "DEAD"


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)

    queue_id = Column(
        Integer,
        ForeignKey("queues.id"),
        nullable=False,
        index=True,
    )

    payload = Column(JSON, nullable=False)

    status = Column(
        SAEnum(JobStatus),
        default=JobStatus.QUEUED,
        nullable=False,
        index=True,
    )

    priority = Column(Integer, default=1)

    scheduled_at = Column(DateTime, nullable=True)

    available_at = Column(DateTime, default=datetime.utcnow)

    worker_id = Column(
        Integer,
        ForeignKey("workers.id"),
        nullable=True,
    )

    attempt = Column(Integer, default=0)

    max_attempts = Column(Integer, default=3)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    completed_at = Column(DateTime)

    queue = relationship(
        "Queue",
        back_populates="jobs"
    )

    worker = relationship(
        "Worker",
        back_populates="jobs"
    )