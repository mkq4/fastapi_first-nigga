import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Starting lifespan")
    yield
    print("Stopping lifespan")
    await delete_tables()
    yield
    print("Off")

app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
