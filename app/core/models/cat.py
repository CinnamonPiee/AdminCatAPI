from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Breed(Base):
    __tablename__ = 'breeds'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    kittens = relationship("Kitten", back_populates="breed")


class Kitten(Base):
    __tablename__ = 'kittens'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    color = Column(String, index=True)
    age = Column(Integer)
    description = Column(String)
    breed_id = Column(Integer, ForeignKey('breeds.id'))

    breed = relationship("Breed", back_populates="kittens")
