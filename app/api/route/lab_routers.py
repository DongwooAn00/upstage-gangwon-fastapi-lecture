import os
import time

from fastapi import APIRouter
from fastapi import Depends

from app.deps import get_user_service
from app.models.schemas import UserCreateRequest, UserResponse

# create user
router = APIRouter(prefix="/lab", tags=["lab"])



@router.get("/cpu")
def cpu_burn():

    end = time.time() + 30
    while time.time() < end:
        pass
    return {"status": "cpu burn done"}

@router.get("/mem")
def mem_alloc():
    data = []
    for _ in range(10_000_000):
        data.append("x" * 1024)
    return {"status": "mem alloc done"}