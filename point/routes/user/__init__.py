from fastapi import APIRouter

from .auth import router as auth_router
from .consumer import router as consumer_router
from .employee import router as employee_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth")
router.include_router(consumer_router, prefix="/consumer")
router.include_router(employee_router, prefix="/employee")
