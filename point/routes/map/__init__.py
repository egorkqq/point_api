from fastapi import APIRouter, Depends

from point.auth import get_user

from .place import router as place_router

router = APIRouter(dependencies=[Depends(get_user)])

router.include_router(place_router, prefix="/place")
