from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.security import get_current_user

from app.models.user import User

from app.schemas.job import JobCreate, JobResponse

from app.services.job_service import JobService

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post("", response_model=JobResponse)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        return JobService.create_job(
            db,
            job,
            current_user
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("", response_model=list[JobResponse])
def get_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return JobService.get_jobs(
        db,
        current_user
    )


@router.get("/{job_id}", response_model=JobResponse)
def get_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    job = JobService.get_job(
        db,
        job_id,
        current_user
    )

    if job is None:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job

@router.patch("/{job_id}/retry", response_model=JobResponse)
def retry_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    job = JobService.retry_job(db, job_id, current_user)
    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )
    return job