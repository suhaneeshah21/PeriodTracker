from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.shared.firebase_admin import initialize_firebase
from app.features.anemia.router import router as anemia_router
from app.features.pcos.router import router as pcos_router
from app.features.auth.router import router as auth_router

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    initialize_firebase()
    print("Firebase initialized successfully")

app.include_router(anemia_router, prefix="/api/anemia", tags=["Anemia"])
app.include_router(pcos_router, prefix="/api/pcos", tags=["PCOS"])
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "NariHealth API is running"}