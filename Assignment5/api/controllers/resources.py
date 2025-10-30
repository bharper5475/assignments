from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models, schemas

def create(db: Session, resource: schemas.ResourceCreate):
    db_obj = models.Resource(
        item=resource.item,
        amount=resource.amount
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def read_all(db: Session):
    return db.query(models.Resource).all()

def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update(db: Session, resource_id: int, resource: schemas.ResourceUpdate):
    q = db.query(models.Resource).filter(models.Resource.id == resource_id)
    update_data = resource.model_dump(exclude_unset=True)
    q.update(update_data, synchronize_session=False)
    db.commit()
    return q.first()

def delete(db: Session, resource_id: int):
    q = db.query(models.Resource).filter(models.Resource.id == resource_id)
    q.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
