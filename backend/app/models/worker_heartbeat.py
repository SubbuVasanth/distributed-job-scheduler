from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.base import Base


class WorkerHeartbeat(Base):
    __tablename__ = "worker_heartbeats"

    id = Column(Integer, primary_key=True)

    worker_id = Column(
        Integer,
        ForeignKey("workers.id"),
        nullable=False,
    )

    heartbeat_time = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    worker = relationship(
        "Worker",
        back_populates="heartbeats"
    )