from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from backend.api.status import status
from backend.api.users import users
from backend.api.item import item
from backend.api.category import category
from backend.api.inventory_location import inventory_location
from backend.api.item_info import item_info

app = FastAPI()

origins = [
    "http://localhost", "http://localhost:8000", "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "🏡Welcome to home inventory😀"}


app.include_router(users.router)
app.include_router(item.router)
app.include_router(item_info.router)
app.include_router(category.router)
app.include_router(status.router)
app.include_router(inventory_location.router)
