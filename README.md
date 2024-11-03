# Construir la imagen 
## docker build -t api .

# Ejecutar el Contenedor de Docker
## docker run -d -p 5000:5000 flask-api   

# Verificar que este en ejecución
## docker ps


# Crear entorno visual
## python3 -m venv .venv //linux(WSL)


# Iniciar el entorno virtual
## .venv\Scripts\Activate 

---------------------------------------------------------------------
# ruta Jenkins
## http://localhost:8080/

# Resultados de las Pruebas de la API en Jenkins

## Capturas de Pantalla de Jenkins

![Pipeline Test-api-Jenkins](ScreenShots/Papeline.png)
![Solicitus web para ver el estado inicial](ScreenShots/Solicitud-Antes-Del-Jenkins.png)
![Proceso dela prueba](ScreenShots/Git-Despendencias-Test-Publicación.png)
![Papeline Success](ScreenShots/Papeline-Success.png)
![Historial de pruebas Success](ScreenShots/Historial_Success.png)
![Resultados de la solicitud](ScreenShots/Resultados.png)
![Resultados en navegador ya aplicados](ScreenShots/Resultados-Solicitud.png)
