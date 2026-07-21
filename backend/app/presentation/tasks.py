from fastapi import APIRouter
from typing import List
from app.domain.models import Task

# Creamos un "Router" para agrupar todas las acciones relacionadas con Tareas
router = APIRouter(prefix="/tasks", tags=["Gestión de Tareas"])

# ATENCIÓN: Por ahora, usaremos una lista en memoria como "base de datos falsa".
# En el siguiente paso la cambiaremos por una base de datos real.
fake_database: List[Task] = []

@router.post("/", response_model=Task, summary="Crear una nueva tarea")
def create_task(task: Task):
    """Recibe una tarea desde la web y la guarda en nuestra base de datos."""
    # Como aún no tenemos base de datos real, le asignamos un ID temporal
    task.id = len(fake_database) + 1
    fake_database.append(task)
    return task

@router.get("/", response_model=List[Task], summary="Obtener todas las tareas")
def get_tasks():
    """Devuelve la lista completa de tareas guardadas."""
    return fake_database

@router.put("/{task_id}", response_model=Task, summary="Actualizar una tarea")
def update_task(task_id: int, updated_task: Task):
    """Busca una tarea por su ID y actualiza sus datos."""
    for index, task in enumerate(fake_database):
        if task.id == task_id:
            updated_task.id = task_id # Mantenemos el ID original
            fake_database[index] = updated_task
            return updated_task
    return {"error": "Tarea no encontrada"}

@router.delete("/{task_id}", summary="Borrar una tarea")
def delete_task(task_id: int):
    """Elimina una tarea de nuestra base de datos falsa usando su ID."""
    for index, task in enumerate(fake_database):
        if task.id == task_id:
            del fake_database[index]
            return {"message": f"Tarea {task_id} eliminada exitosamente"}
    return {"error": "Tarea no encontrada"}