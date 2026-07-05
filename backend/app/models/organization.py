from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    projects = relationship(
        "Project",
        back_populates="organization"
    )