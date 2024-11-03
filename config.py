# config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URI de conexión a SQL Server
DATABASE_URL = "mssql+pyodbc://login:426671979@EDUARDOB\\SQLEXPRESS/Act?driver=ODBC+Driver+17+for+SQL+Server"

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL)

# Crear la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
