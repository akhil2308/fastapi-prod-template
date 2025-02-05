import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.api import router as api_router

from database import engine
from settings import logging_config,  ALLOWED_HOSTS
from fastapi.logger import logger
import logging

# uvicorn and gunicorn uniform logs
gunicorn_error_logger           = logging.getLogger("gunicorn.error")
gunicorn_logger                 = logging.getLogger("gunicorn")
uvicorn_access_logger           = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers  = gunicorn_error_logger.handlers
logger.handlers                 = gunicorn_error_logger.handlers
logger.setLevel("INFO")

logging.config.dictConfig(logging_config)


app = FastAPI(
    title="FastAPI Template",
    description="",
    version="1.0.0",
    docs_url="/",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info", reload=True)#, log_config=logging_config
