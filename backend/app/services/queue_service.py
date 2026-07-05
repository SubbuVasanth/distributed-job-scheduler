from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.queue import Queue
from app.models.user import User


class QueueService:

    @staticmethod
    def create_queue(db: Session, queue_data, current_user: User):

        project = (
            db.query(Project)
            .filter(
                Project.id == queue_data.project_id,
                Project.owner_id == current_user.id
            )
            .first()
        )

        if project is None:
            raise ValueError("Project not found")

        queue = Queue(
            project_id=queue_data.project_id,
            name=queue_data.name,
            priority=queue_data.priority,
            max_concurrency=queue_data.max_concurrency,
            retry_policy_id=queue_data.retry_policy_id,
        )

        db.add(queue)
        db.commit()
        db.refresh(queue)

        return queue

    @staticmethod
    def get_queues(db: Session, current_user: User):

        return (
            db.query(Queue)
            .join(Project)
            .filter(Project.owner_id == current_user.id)
            .all()
        )

    @staticmethod
    def pause_queue(db: Session, queue_id: int):

        queue = db.query(Queue).filter(Queue.id == queue_id).first()

        if queue is None:
            return None

        queue.is_paused = True

        db.commit()

        return queue

    @staticmethod
    def resume_queue(db: Session, queue_id: int):

        queue = db.query(Queue).filter(Queue.id == queue_id).first()

        if queue is None:
            return None

        queue.is_paused = False

        db.commit()

        return queue