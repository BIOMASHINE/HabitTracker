from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from actions.create_superuser import create_superuser
from core.config import settings

from api import router as api_router
from core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await create_superuser()
    yield
    # shutdown
    await db_helper.dispose()

main_app = FastAPI(
    default_response_class=ORJSONResponse,
    redirect_slashes=False,
    lifespan=lifespan,
)
main_app.include_router(
    api_router,
)

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "https://track-your-life.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(
        'main:main_app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )
