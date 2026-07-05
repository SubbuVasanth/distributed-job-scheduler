from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.security import get_current_user

from app.models.user import User

from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
)

from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post(
    "",
    response_model=ProjectResponse
)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return ProjectService.create_project(
        db,
        project,
        current_user
    )


@router.get(
    "",
    response_model=list[ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return ProjectService.get_projects(
        db,
        current_user
    )


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = ProjectService.delete_project(
        db,
        project_id,
        current_user
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {"message": "Project deleted"}