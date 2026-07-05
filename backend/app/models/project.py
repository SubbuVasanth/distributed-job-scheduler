from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship

from app.models.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False)

    description = Column(String(255))

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )

    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship(
        "User",
        back_populates="projects"
    )

    organization = relationship(
        "Organization",
        back_populates="projects"
    )

    queues = relationship(
        "Queue",
        back_populates="project"
    )