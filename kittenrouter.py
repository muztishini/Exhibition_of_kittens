from fastapi import APIRouter
from models import Kitten, SessionLocal
from fastapi.responses import JSONResponse
from schemas import KittensOutSchema, KittenSchema
from typing import List


kitten_router = APIRouter()
db = SessionLocal()


@kitten_router.get("/", response_model=List[KittensOutSchema])
async def get_kittens():
    kittens = db.query(Kitten).all()
    return kittens


@kitten_router.get("/{id}", response_model=KittensOutSchema)
async def get_kitten(id: int):
    kitten = db.query(Kitten).filter(Kitten.id == id).first()
    if kitten is None:
        return JSONResponse(status_code=404, content={"message": f"Информация о котенке с id {id} не найдена"})
    return kitten


@kitten_router.post('/')
async def create_kitten(kitten_in: KittenSchema):
    kitten = Kitten(**kitten_in.model_dump())
    db.add(kitten)
    db.commit()
    db.refresh(kitten)
    return {"message": "Информация о котенке добавлена", "data": kitten}


@kitten_router.put("/{id}")
async def update_kitten(id: int, kitten_in: KittenSchema):
    kitten_query = db.query(Kitten).filter(Kitten.id == id)
    kitten_new = kitten_query.first()
    if kitten_new is None:
        return JSONResponse(status_code=404, content={"message": f"Информация о котенке с id {id} не найдена"})
    kitten_query.update(kitten_in.model_dump())
    db.commit()
    db.refresh(kitten_new)
    return {"message": "Информация о котенке обновлена", "data": kitten_new}


@kitten_router.delete("/{id}")
async def delete_kitten(id: int):
    kitten = db.query(Kitten).filter(Kitten.id == id).first()
    if kitten is None:
        return JSONResponse(status_code=404, content={"message": f"Информация о котенке с id {id} не найдена"})
    db.delete(kitten)
    db.commit()
    return {"message": f"Информация о котенке с id {id} удалена!"}
