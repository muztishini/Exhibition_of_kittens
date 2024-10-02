from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()


class Breed(Base):
    __tablename__ = 'breeds'
    
    id = Column(Integer, primary_key=True, index=True)
    breedname = Column(String(50), nullable=False)
    kitten = relationship("Kitten", back_populates="breed")


class Kitten(Base):
    __tablename__ = 'kittens'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    color = Column(String(20), nullable=False)
    description = Column(String(250), nullable=False)
    breed_id = Column(Integer, ForeignKey("breeds.id"))
    breed = relationship("Breed", back_populates="kitten")
    

Base.metadata.create_all(bind=engine)
