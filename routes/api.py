from fastapi import APIRouter
from src.endpoints import api_service
from src.endpoints import item_service

router = APIRouter()
router.include_router(api_service.router)
router.include_router(item_service.router)