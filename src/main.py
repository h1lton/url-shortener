from fastapi import FastAPI

from src.shortener.router import router as shortener_router

app = FastAPI()

app.include_router(shortener_router)


@app.get("/")
async def check():
    return "The server is working"
