from sqlalchemy import Column, Integer, String, DateTime, Time
from app.infrastructure.database import Base

class DBTask(Base):
    """Tabla de tareas en la base de datos SQLite."""
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    priority = Column(Integer, default=1)
    status = Column(String, default="pendiente")
    due_date = Column(DateTime, nullable=True)

class DBScheduleBlock(Base):
    """Tabla de horarios en la base de datos SQLite."""
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    day_of_week = Column(Integer)
    start_time = Column(Time)
    end_time = Column(Time)