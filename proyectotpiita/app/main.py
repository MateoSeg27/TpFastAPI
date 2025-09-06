from fastapi import FastAPI,HTTPException

app = FastAPI()

# "Base de datos" en memoria (solo lista)
tasks = []

# Ruta principal
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Tareas"}

# Obtener todas las tareas
@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

# Crear una tarea
@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return {"message": "Tarea agregada", "task": task}
