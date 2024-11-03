# test_api.py
import requests

# URL base de la API (asegúrarse que esté en ejecución)
BASE_URL = "http://127.0.0.1:8000"

# Pruebas para el endpoint de actividades
def test_create_activity():
    """Prueba para crear una nueva actividad"""
    response = requests.post(f"{BASE_URL}/activities/", json={
        "name": "Taller de Programación",
        "total_hours": 20
    })
    print("Create Activity Response:", response.json())

def test_get_activities():
    """Prueba para obtener todas las actividades"""
    response = requests.get(f"{BASE_URL}/activities/")
    print("Get Activities Response:", response.json())

def test_update_activity(activity_id):
    """Prueba para actualizar una actividad existente"""
    response = requests.put(f"{BASE_URL}/activities/{activity_id}", json={
        "name": "Taller de Programación Avanzada",
        "total_hours": 30
    })
    print("Update Activity Response:", response.json())

def test_delete_activity(activity_id):
    """Prueba para eliminar una actividad de forma lógica"""
    response = requests.delete(f"{BASE_URL}/activities/{activity_id}")
    print("Delete Activity Response:", response.json())

# Pruebas para el endpoint de estudiantes
def test_create_student():
    """Prueba para crear un nuevo estudiante"""
    response = requests.post(f"{BASE_URL}/students/", json={
        "student_id": 12345,
        "full_name": "Ana Gomez",
        "major": "Ingeniería en Sistemas",
        "semester": 5,
        "age": 21,
        "complementary_credits": 2
    })
    print("Create Student Response:", response.json())

def test_get_students():
    """Prueba para obtener todos los estudiantes"""
    response = requests.get(f"{BASE_URL}/students/")
    print("Get Students Response:", response.json())

def test_update_student(student_id):
    """Prueba para actualizar un estudiante existente"""
    response = requests.put(f"{BASE_URL}/students/{student_id}", json={
        "full_name": "Ana Gomez Actualizada",
        "age": 22
    })
    print("Update Student Response:", response.json())

def test_delete_student(student_id):
    """Prueba para eliminar un estudiante de forma lógica"""
    response = requests.delete(f"{BASE_URL}/students/{student_id}")
    print("Delete Student Response:", response.json())

# Pruebas para el endpoint de maestros
def test_create_teacher():
    """Prueba para crear un nuevo maestro"""
    response = requests.post(f"{BASE_URL}/teachers/", json={
        "teacher_id": 56789,
        "full_name": "Carlos Perez",
        "activity_id": 1  
d exista
    })
    print("Create Teacher Response:", response.json())

def test_get_teachers():
    """Prueba para obtener todos los maestros"""
    response = requests.get(f"{BASE_URL}/teachers/")
    print("Get Teachers Response:", response.json())

def test_update_teacher(teacher_id):
    """Prueba para actualizar un maestro existente"""
    response = requests.put(f"{BASE_URL}/teachers/{teacher_id}", json={
        "full_name": "Carlos Perez Actualizado"
    })
    print("Update Teacher Response:", response.json())

def test_delete_teacher(teacher_id):
    """Prueba para eliminar un maestro de forma lógica"""
    response = requests.delete(f"{BASE_URL}/teachers/{teacher_id}")
    print("Delete Teacher Response:", response.json())

# Pruebas para el endpoint de clases en progreso
def test_create_in_progress():
    """Prueba para crear una nueva clase en progreso"""
    response = requests.post(f"{BASE_URL}/in_progress/", json={
        "student_id": 12345,  
te exista
        "teacher_id": 56789,  
exista
        "day_of_week": "Lunes",
        "schedule": "10:00 - 12:00",
        "hours_completed": 10,
        "hours_pending": 20
    })
    print("Create In Progress Response:", response.json())

def test_get_in_progress():
    """Prueba para obtener todas las clases en progreso"""
    response = requests.get(f"{BASE_URL}/in_progress/")
    print("Get In Progress Response:", response.json())

def test_update_in_progress(course_id):
    """Prueba para actualizar una clase en progreso existente"""
    response = requests.put(f"{BASE_URL}/in_progress/{course_id}", json={
        "hours_completed": 15,
        "hours_pending": 15
    })
    print("Update In Progress Response:", response.json())

def test_delete_in_progress(course_id):
    """Prueba para eliminar una clase en progreso de forma lógica"""
    response = requests.delete(f"{BASE_URL}/in_progress/{course_id}")
    print("Delete In Progress Response:", response.json())

# Ejecutar todas las pruebas
if __name__ == "__main__":
    # Actividades
    #test_create_activity()
    test_get_activities()
    test_update_activity(1)  
    #test_delete_activity(1)  

    # Estudiantes
    #test_create_student()
    #test_get_students()
    #test_update_student(12345)  
    #test_delete_student(12345)  

    # Maestros
    #test_create_teacher()
    #test_get_teachers()
    #test_update_teacher(56789)  
    #test_delete_teacher(56789)  

    # Clases en Progreso
    #test_create_in_progress()
    #test_get_in_progress()
    #test_update_in_progress(1)  
    #test_delete_in_progress(1)  