from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware
from routes.upload_pdfs import router as upload_router
from routes.ask_question import router as ask_router
from dotenv import load_dotenv
import os
import base64

# Load .env file for local development
load_dotenv()

# Decode base64 credentials (for Render deployment)
if "GOOGLE_CREDENTIALS_BASE64" in os.environ:
    credentials_path = "/tmp/gcloud_key.json"
    with open(credentials_path, "wb") as f:
        f.write(base64.b64decode(os.environ["GOOGLE_CREDENTIALS_BASE64"]))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

# FastAPI setup
app = FastAPI(
    title="Medical Assistant API",
    description="API for AI Medical Assistant Chatbot"
)

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# middleware exception handlers
app.middleware("http")(catch_exception_middleware)

# routers
app.include_router(upload_router)  # 1. upload pdfs documents
app.include_router(ask_router)     # 2. asking query
