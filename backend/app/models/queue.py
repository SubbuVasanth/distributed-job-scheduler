from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import relationship

from app.models.base import Base


class Queue(Base):
    __tablename__ = "queues"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False)

    priority = Column(Integer, default=1)

    max_concurrency = Column(Integer, default=5)

    is_paused = Column(Boolean, default=False)

    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False
    )

    retry_policy_id = Column(
        Integer,
        ForeignKey("retry_policies.id"),
        nullable=False
    )

    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship(
        "Project",
        back_populates="queues"
    )

    retry_policy = relationship(
        "RetryPolicy",
        back_populates="queues"
    )

    jobs = relationship(
        "Job",
        back_populates="queue"
    )