from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class DeadLetterQueue(Base):
    __tablename__ = "dead_letter_queue"

    id = Column(Integer, primary_key=True)

    job_id = Column(
        Integer,
        ForeignKey("jobs.id"),
        nullable=False,
        unique=True,
    )

    failure_reason = Column(String(500))

    failed_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    job = relationship("Job")