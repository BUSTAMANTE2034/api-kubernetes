import os
import sys

# Agregar la carpeta raíz a sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api import create_app  # Asegúrate de que esta importación esté correcta

app = create_app()  # Crea la aplicación

if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar en modo debug para desarrollo
