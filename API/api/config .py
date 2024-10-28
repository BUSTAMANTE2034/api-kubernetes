import os
class Config:
    # URL de la base de datos
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://login:426671979@EDUARDOB\\SQLEXPRESS/AEE?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar el seguimiento de modificaciones
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta'  # Clave secreta para sesiones

    # Otras configuraciones que puedes añadir
    DEBUG = True  # Activar modo de depuración
    TESTING = False  # Desactivar pruebas (cambiar a True durante las pruebas)
