from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app.domain.models import ScheduleBlock
from app.infrastructure.models import DBScheduleBlock
from app.infrastructure.database import get_db

router = APIRouter(prefix="/schedules", tags=["Gestión de Horario"])

@router.post("/", response_model=ScheduleBlock, summary="Crear un bloque de clase")
def create_schedule(block: ScheduleBlock, db: Session = Depends(get_db)):
    """Guarda una nueva clase permanentemente en SQLite."""
    db_block = DBScheduleBlock(
        title=block.title,
        day_of_week=block.day_of_week,
        start_time=block.start_time,
        end_time=block.end_time
    )
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block

@router.get("/", response_model=List[ScheduleBlock], summary="Ver mi horario")
def get_schedules(db: Session = Depends(get_db)):
    """Lee todas las clases desde la base de datos."""
    return db.query(DBScheduleBlock).all()