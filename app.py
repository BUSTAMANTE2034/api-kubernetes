# app.py
from fastapi import FastAPI
from routes import router

app = FastAPI()

# Incluir las rutas
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
