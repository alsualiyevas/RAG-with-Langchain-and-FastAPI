from fastapi import FastAPI 
from app.config import settings 
app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION) 
@app.get("/") 
def root(): return {"message": "RAG API is online"} 
