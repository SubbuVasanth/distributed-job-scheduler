from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.security import get_current_user

from app.models.user import User

from app.schemas.queue import (
    QueueCreate,
    QueueResponse
)

from app.services.queue_service import QueueService

router = APIRouter(
    prefix="/queues",
    tags=["Queues"]
)


@router.post("", response_model=QueueResponse)
def create_queue(
    queue: QueueCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:
        return QueueService.create_queue(
            db,
            queue,
            current_user
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("", response_model=list[QueueResponse])
def get_queues(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return QueueService.get_queues(
        db,
        current_user
    )


@router.patch("/{queue_id}/pause")
def pause_queue(
    queue_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    queue = QueueService.pause_queue(db, queue_id)

    if queue is None:
        raise HTTPException(
            status_code=404,
            detail="Queue not found"
        )

    return {
        "message": "Queue paused successfully",
        "queue_id": queue.id,
        "is_paused": queue.is_paused
    }

@router.patch("/{queue_id}/resume")
def resume_queue(
    queue_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    queue = QueueService.resume_queue(db, queue_id)

    if queue is None:
        raise HTTPException(
            status_code=404,
            detail="Queue not found"
        )

    return {
        "message": "Queue resumed successfully",
        "queue_id": queue.id,
        "is_paused": queue.is_paused
    }