from fastapi import APIRouter
from models import Breed, Kitten, SessionLocal
from fastapi.responses import JSONResponse
from schemas import BreedSchema, KittensOutSchema
from typing import List


breed_router = APIRouter()
db = SessionLocal()


@breed_router.get("/", response_model=List[BreedSchema])
async def get_breeds():
    breeds = db.query(Breed).all()
    return breeds


@breed_router.get("/{id}", response_model=List[KittensOutSchema])
async def get_kittens_by_breed(id: int):
    kittens = db.query(Kitten).filter(Kitten.breed_id == id).all()
    if not kittens:
        return JSONResponse(status_code=404, content={"message": f"Котят такой породы не обнаружено"})
    return kittens
