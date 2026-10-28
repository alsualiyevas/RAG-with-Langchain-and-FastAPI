import os 
from pydantic_settings import BaseSettings 
class Settings(BaseSettings): 
    PROJECT_NAME: str = "Enterprise RAG Knowledge API" 
    VERSION: str = "1.0.0" 
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "") 
settings = Settings() 
