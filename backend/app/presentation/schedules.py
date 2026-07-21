from fastapi import APIRouter
from typing import List
from app.domain.models import ScheduleBlock

router = APIRouter(prefix="/schedules", tags=["Gestión de Horario"])

# Base de datos temporal para los horarios
fake_schedule_db: List[ScheduleBlock] = []

@router.post("/", response_model=ScheduleBlock, summary="Crear un bloque de clase")
def create_schedule(block: ScheduleBlock):
    """Guarda una nueva clase en tu horario semanal."""
    block.id = len(fake_schedule_db) + 1
    fake_schedule_db.append(block)
    return block

@router.get("/", response_model=List[ScheduleBlock], summary="Ver mi horario")
def get_schedules():
    """Devuelve todas las clases guardadas."""
    return fake_schedule_db