from fastapi import FastAPI
from models import SessionLocal, Kitten, Breed
from schemas import BreedSchema, KittenSchema, KittensOutSchema
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()
db = SessionLocal()


@app.get("/api/breeds", response_model=List[BreedSchema])
async def get_breeds():
    breeds = db.query(Breed).all()
    return breeds


@app.get("/api/kittens", response_model=List[KittensOutSchema])
async def get_kittens():
    kittens = db.query(Kitten).all()
    return kittens


@app.get("/api/kittens/{id}", response_model=KittensOutSchema)
async def get_kitten(id: int):
    kitten = db.query(Kitten).filter(Kitten.id == id).first()
    if kitten is None:
        return JSONResponse(status_code=404, content={"message": f"Котенок с id {id} не найден"})
    return kitten


@app.post('/api/kittens')
async def create_kitten(kitten_in: KittenSchema):
    kitten = Kitten(**kitten_in.model_dump())
    db.add(kitten)
    db.commit()
    db.refresh(kitten)
    return {"message": "Котенок добавлен", "data": kitten}


@app.put("/api/kittens/{id}")
async def update_kittens(id: int, kitten_in: KittenSchema):
    kitten_query = db.query(Kitten).filter(Kitten.id == id)
    update_kitten = kitten_query.first()
    if update_kitten is None:
        return JSONResponse(status_code=404, content={"message": f"Котенок с id {id} не найден"})
    kitten_query.update(kitten_in.model_dump())
    db.commit()
    db.refresh(update_kitten)
    return {"message": "Котенок обновлен", "data": update_kitten}


@app.delete("/api/kittens/{id}")
async def delete_kitten(id: int):
    kitten = db.query(Kitten).filter(Kitten.id == id).first()
    if kitten is None:
        return JSONResponse(status_code=404, content={"message": f"Котенок с id {id} не найден"})
    db.delete(kitten)
    db.commit()
    return {"message": f"Котенок с id {id} удален!"}
