from fastapi import APIRouter, Depends

from point.auth import get_user

from .establishment import router as establishment_router
from .place import router as place_router

router = APIRouter(dependencies=[Depends(get_user)])

router.include_router(establishment_router, prefix="/establishment")
router.include_router(place_router, prefix="/place")
