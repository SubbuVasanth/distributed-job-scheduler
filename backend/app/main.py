from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.scheduler.cron_scheduler import start_scheduler

from app.api.auth import router as auth_router
from app.api.projects import router as project_router
from app.api.queues import router as queue_router
from app.api.jobs import router as job_router

app = FastAPI(
    title="Distributed Job Scheduler"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(project_router)
app.include_router(queue_router)
app.include_router(job_router)

start_scheduler()
