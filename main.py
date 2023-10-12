from fastapi import FastAPI

from config import HOST, PORT
from gisdatabase import database
from routers import routers

from starlette.testclient import TestClient
import pytest



app = FastAPI()

app.include_router(routers.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client
