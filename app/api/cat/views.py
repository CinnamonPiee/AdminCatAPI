from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import crud
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/breeds/")
def read_breeds(db: Session = Depends(get_db)):
    return crud.get_breeds(db)


@app.get("/kittens/")
def read_kittens(db: Session = Depends(get_db)):
    return crud.get_kittens(db)


@app.get("/kittens/{breed_id}")
def read_kittens_by_breed(breed_id: int, db: Session = Depends(get_db)):
    return crud.get_kittens_by_breed(db, breed_id)


@app.get("/kitten/{kitten_id}")
def read_kitten(kitten_id: int, db: Session = Depends(get_db)):
    return crud.get_kitten(db, kitten_id)


@app.post("/kitten/")
def create_kitten(kitten: schemas.KittenCreate, db: Session = Depends(get_db)):
    return crud.create_kitten(db, kitten)


@app.put("/kitten/{kitten_id}")
def update_kitten(kitten_id: int, kitten: schemas.KittenUpdate, db: Session = Depends(get_db)):
    return crud.update_kitten(db, kitten_id, kitten)


@app.delete("/kitten/{kitten_id}")
def delete_kitten(kitten_id: int, db: Session = Depends(get_db)):
    return crud.delete_kitten(db, kitten_id)
