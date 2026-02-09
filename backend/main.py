from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API de Aladino activa", "estado": "Operacional", "servidor": "Ubuntu 22.04"}

@app.get("/status")
def get_status():
    # Aquí es donde en el futuro conectaremos tu script de diagnóstico
    return {"cpu": "Core 2 Quad", "status": "Online"}
