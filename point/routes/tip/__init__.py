from fastapi import APIRouter

from .asset import router as asset_router
from .receiver import router as receiver_router

router = APIRouter(tags=["Tip"])

router.include_router(asset_router, prefix="/asset")
router.include_router(receiver_router, prefix="/receiver")
