from typing import List
from app.domain.models import ScheduleBlock

def calculate_busy_minutes(schedules: List[ScheduleBlock], day_of_week: int) -> int:
    """
    Recorre las clases de un día específico y calcula cuántos minutos en total estás ocupado.
    """
    busy_minutes = 0
    for block in schedules:
        if block.day_of_week == day_of_week:    
            # Convertimos las horas a minutos para hacer la matemática más fácil
            start_total_minutes = (block.start_time.hour * 60) + block.start_time.minute
            end_total_minutes = (block.end_time.hour * 60) + block.end_time.minute
            
            # Sumamos la duración de esta clase
            busy_minutes += (end_total_minutes - start_total_minutes)
            
    return busy_minutes