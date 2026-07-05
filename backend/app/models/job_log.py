from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class JobLog(Base):
    __tablename__ = "job_logs"

    id = Column(Integer, primary_key=True)

    job_execution_id = Column(
        Integer,
        ForeignKey("job_executions.id"),
        nullable=False,
    )

    level = Column(String(20))

    message = Column(String(1000))

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    execution = relationship("JobExecution")