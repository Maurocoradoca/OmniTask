from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.infrastructure.models import DBScheduleBlock
from app.application.time_service import calculate_busy_minutes

router = APIRouter(prefix="/analytics", tags=["Análisis de Tiempo y Productividad"])

@router.get("/free-time/{day_of_week}", summary="Calcular mi tiempo libre")
def get_daily_free_time(day_of_week: int, db: Session = Depends(get_db)):
    """Calcula el tiempo libre leyendo las clases desde SQLite."""
    
    # 1. Traemos SOLO las clases de ese día específico desde la base de datos
    daily_schedules = db.query(DBScheduleBlock).filter(DBScheduleBlock.day_of_week == day_of_week).all()
    
    # 2. Calculamos los minutos ocupados
    busy_minutes = calculate_busy_minutes(daily_schedules, day_of_week)
    
    # 3. Asumimos 16 horas despierto al día (960 minutos)
    total_awake_minutes = 16 * 60 
    
    # 4. Calculamos el tiempo libre
    free_minutes = total_awake_minutes - busy_minutes
    
    return {
        "day_of_week": day_of_week,
        "total_awake_hours": 16.0,
        "busy_hours": round(busy_minutes / 60, 2),
        "free_hours": round(free_minutes / 60, 2),
        "message": "¡Este es el tiempo que tienes para tareas, gimnasio y descanso!"
    }