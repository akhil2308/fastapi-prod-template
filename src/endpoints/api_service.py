from fastapi import APIRouter, HTTPException, Depends, Body
from fastapi import Query

from sqlalchemy.orm import Session
from typing import Optional, Any

from database import get_db

import logging
logger = logging.getLogger(__name__)

# APIRouter creates path operations for user module
router = APIRouter(
    prefix="/api",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.get("/status")
async def status_check():
    return {"status": "Service is up and running!"}

