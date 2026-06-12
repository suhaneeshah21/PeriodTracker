from firebase_admin import auth
from fastapi import HTTPException

def verify_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

def get_current_user(token: str):
    decoded = verify_token(token)
    return {
        "uid": decoded["uid"],
        "email": decoded.get("email")
    }