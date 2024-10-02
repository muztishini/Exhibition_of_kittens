from pydantic import BaseModel, field_validator


class BreedSchema(BaseModel):
    id: int = None
    breedname: str
    

class KittenSchema(BaseModel):
    name: str
    age: int
    color: str
    description: str
    breed_id: int
    
    @field_validator('age')
    def age_must_be_positive(self, value):
        if value <= 0:
            raise ValueError("Возраст котенка должен быть больше 0")
        return value
    
    @field_validator('breed_id')
    def breedid_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Id породы должен быть больше нуля")
        return value

 
class KittensOutSchema(KittenSchema):
    id: int
      