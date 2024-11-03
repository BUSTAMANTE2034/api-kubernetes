from sqlalchemy import create_engine, inspect

# URI de la base de datos
url = "mssql+pyodbc://login:426671979@EDUARDOB\\SQLEXPRESS/Act?driver=ODBC+Driver+17+for+SQL+Server"

# Crear la conexión a la base de datos
engine = create_engine(url)

try:
    # Conectar a la base de datos y obtener el inspector
    with engine.connect() as connection:
        inspector = inspect(engine)

        # Listar las tablas disponibles
        tables = inspector.get_table_names()
        if tables:
            print("Conexión exitosa. Tablas en la base de datos:")
            for table in tables:
                print(f"- {table}")
        else:
            print("Conexión exitosa, pero no se encontraron tablas en la base de datos.")
except Exception as e:
    print("Error al conectar con la base de datos:", e)
