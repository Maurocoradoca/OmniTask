from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from datetime import datetime, time

class Task(BaseModel):
    """
    Modelo de Dominio para una Tarea.
    Pydantic (BaseModel) nos ayuda a validar automáticamente 
    que los datos que entren a nuestra API sean correctos.
    """
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=100, description="Título de la tarea")
    description: Optional[str] = Field(None, description="Detalles adicionales")
    
    # 1: Baja, 2: Media, 3: Alta. Usamos 'ge' (greater/equal) y 'le' (less/equal) para limitar los valores.
    priority: int = Field(default=1, ge=1, le=3) 
    
    # Estados permitidos: "pendiente", "en_progreso", "completada"
    status: str = Field(default="pendiente") 
    
    due_date: Optional[datetime] = None

class ScheduleBlock(BaseModel):
    """
    Modelo para un bloque de horario fijo (ej. Clases de la universidad).
    """
    id: Optional[int] = None
    title: str = Field(..., description="Nombre de la clase (Ej. Cálculo I)")
    # Usaremos números para los días: 1=Lunes, 2=Martes ... 7=Domingo
    day_of_week: int = Field(..., ge=1, le=7, description="Día de la semana")
    start_time: time = Field(..., description="Hora de inicio (Formato HH:MM:SS)")
    end_time: time = Field(..., description="Hora de fin (Formato HH:MM:SS)")