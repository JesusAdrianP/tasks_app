from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.task import Task
from app.models.user import User
from app.models.task import TaskStatus 

#script to seed the database with intial tasks
def seed_tasks():
    db: Session = SessionLocal()
    try:
        # get the first user to assing tasks to
        user = db.query(User).first()
        if not user:
            print("No se encontró ningún usuario. Crea primero un usuario.")
            return

        tasks_data = [
            {"title": f"Tarea {i+1}", "description": f"Descripción de la tarea {i+1}", "status": TaskStatus.pending, "created_by": user.id}
            for i in range(20)
        ]

        for data in tasks_data:
            task = Task(
                title=data["title"],
                description=data["description"],
                status=data["status"],
                created_by=data["created_by"],
                created_at=datetime.now(tz=timezone.utc),
                updated_at=datetime.now(tz=timezone.utc)
            )
            db.add(task)

        db.commit()
        print("20 tareas insertadas correctamente!")
    except Exception as e:
        print("Error al insertar tareas:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_tasks()
