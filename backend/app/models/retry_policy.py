from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Enum as SAEnum, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class RetryStrategy(str, Enum):
    FIXED = "FIXED"
    LINEAR = "LINEAR"
    EXPONENTIAL = "EXPONENTIAL"


class RetryPolicy(Base):
    __tablename__ = "retry_policies"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False, unique=True)

    strategy = Column(
        SAEnum(RetryStrategy),
        nullable=False,
        default=RetryStrategy.FIXED
    )

    max_retries = Column(Integer, nullable=False, default=3)

    delay_seconds = Column(Integer, nullable=False, default=5)

    backoff_multiplier = Column(Integer, nullable=False, default=2)

    created_at = Column(DateTime, default=datetime.utcnow)

    queues = relationship(
        "Queue",
        back_populates="retry_policy"
    )