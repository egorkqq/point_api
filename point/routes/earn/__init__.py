from fastapi import APIRouter

from .referral import router as referral_router
from .task import router as task_router

router = APIRouter(tags=["Earn"])

router.include_router(referral_router, prefix="/referral")
router.include_router(task_router, prefix="/task")
