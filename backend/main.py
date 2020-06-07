from fastapi import FastAPI

from backend.api import (users, item_info, item, category, status,
                         inventory_location)

app = FastAPI()


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