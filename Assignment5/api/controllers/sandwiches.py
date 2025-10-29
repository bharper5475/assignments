from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models, schemas

def create(db: Session, sandwich: schemas.SandwichCreate):
    db_obj = models.Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich_id: int, sandwich: schemas.SandwichUpdate):
    q = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    update_data = sandwich.model_dump(exclude_unset=True)
    q.update(update_data, synchronize_session=False)
    db.commit()
    return q.first()

def delete(db: Session, sandwich_id: int):
    q = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    q.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

