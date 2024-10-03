from fastapi import FastAPI
from breedrouter import breed_router
from kittenrouter import kitten_router


app = FastAPI()


app.include_router(breed_router, prefix="/api/breeds", tags=["Breeds methods"])
app.include_router(kitten_router, prefix="/api/kittens", tags=["Kittens methods"])
