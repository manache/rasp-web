from fastapi import FastAPI
from backend.api import ruby_exec

app = FastAPI()
app.include_router(ruby_exec.router, prefix="/api")
