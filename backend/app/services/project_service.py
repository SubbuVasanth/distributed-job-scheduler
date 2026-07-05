from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.user import User


class ProjectService:

    @staticmethod
    def create_project(
        db: Session,
        project,
        current_user: User
    ):

        new_project = Project(
            name=project.name,
            description=project.description,
            owner_id=current_user.id,

            # Temporary
            organization_id=1
        )

        db.add(new_project)

        db.commit()

        db.refresh(new_project)

        return new_project

    @staticmethod
    def get_projects(
        db: Session,
        current_user: User
    ):

        return (
            db.query(Project)
            .filter(Project.owner_id == current_user.id)
            .all()
        )

    @staticmethod
    def delete_project(
        db: Session,
        project_id: int,
        current_user: User
    ):

        project = (
            db.query(Project)
            .filter(
                Project.id == project_id,
                Project.owner_id == current_user.id
            )
            .first()
        )

        if project is None:
            return None

        db.delete(project)

        db.commit()

        return True