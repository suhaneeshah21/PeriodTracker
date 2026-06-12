from fastapi import APIRouter, Header
from app.features.auth.service import get_current_user

router = APIRouter()

@router.post("/verify")
def verify(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    return get_current_user(token)