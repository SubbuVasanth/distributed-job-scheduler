from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Enum as SAEnum, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class WorkerStatus(str, Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    BUSY = "BUSY"


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False)

    hostname = Column(String(255), nullable=False)

    status = Column(
        SAEnum(WorkerStatus),
        default=WorkerStatus.ONLINE,
        nullable=False,
    )

    started_at = Column(DateTime, default=datetime.utcnow)

    last_seen = Column(DateTime, default=datetime.utcnow)

    jobs = relationship(
        "Job",
        back_populates="worker"
    )

    heartbeats = relationship(
        "WorkerHeartbeat",
        back_populates="worker",
        cascade="all, delete-orphan"
    )