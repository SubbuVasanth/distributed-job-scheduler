from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any


class JobCreate(BaseModel):
    queue_id: int
    payload: dict[str, Any]

    priority: int = 1

    delay_seconds: int | None = None

    scheduled_at: datetime | None = None

    cron_expression: str | None = None


class JobResponse(BaseModel):
    id: int
    status: str
    priority: int

    model_config = ConfigDict(from_attributes=True)