from pydantic import BaseModel, ConfigDict


class QueueCreate(BaseModel):
    project_id: int
    name: str
    priority: int = 1
    max_concurrency: int = 5
    retry_policy_id: int


class QueueResponse(BaseModel):
    id: int
    name: str
    priority: int
    max_concurrency: int
    is_paused: bool

    model_config = ConfigDict(from_attributes=True)