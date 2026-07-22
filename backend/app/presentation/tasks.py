from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.domain.models import Task
from app.infrastructure.models import DBTask
from app.infrastructure.database import get_db

router = APIRouter(prefix="/tasks", tags=["Gestión de Tareas"])


@router.post("/", response_model=Task, summary="Crear una nueva tarea")
def create_task(task: Task, db: Session = Depends(get_db)):
    """Guarda una tarea permanentemente en SQLite."""
    db_task = DBTask(
        title=task.title,
        description=task.description,
        priority=task.priority,
        status=task.status,
        due_date=task.due_date
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=List[Task], summary="Obtener todas las tareas")
def get_tasks(db: Session = Depends(get_db)):
    """Lee todas las tareas desde la base de datos."""
    return db.query(DBTask).all()

@router.put("/{task_id}", response_model=Task, summary="Actualizar una tarea")
def update_task(task_id: int, updated_task: Task, db: Session = Depends(get_db)):
    """Busca y actualiza una tarea en la base de datos."""
    db_task = db.query(DBTask).filter(DBTask.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db_task.title = updated_task.title
    db_task.description = updated_task.description
    db_task.priority = updated_task.priority
    db_task.status = updated_task.status
    db_task.due_date = updated_task.due_date
    
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}", summary="Borrar una tarea")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Elimina permanentemente una tarea."""
    db_task = db.query(DBTask).filter(DBTask.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db.delete(db_task)
    db.commit()
    return {"message": f"Tarea {task_id} eliminada exitosamente"}