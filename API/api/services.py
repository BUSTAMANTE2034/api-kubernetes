from flask import Blueprint, request, jsonify
from api.models import db, Actividad, Alumno, Maestro, EnCurso  

# Crear un Blueprint para tus servicios
api = Blueprint('api', __name__)

# --------------------- ENDPOINTS DE ACTIVIDADES --------------------- #
@api.route('/actividades', methods=['GET'])
def get_actividades():
    actividades = Actividades.query.all()
    return jsonify([{
        'id_actividad': a.id_actividad,
        'nombre': a.nombre,
        'horas_totales': a.horas_totales
    } for a in actividades])

@api.route('/actividades', methods=['POST'])
def create_actividad():
    data = request.get_json()
    new_actividad = Actividades(nombre=data['nombre'], horas_totales=data['horas_totales'])
    db.session.add(new_actividad)
    db.session.commit()
    return jsonify({'message': 'Actividad creada', 'id': new_actividad.id_actividad}), 201

@api.route('/actividades/<int:id>', methods=['PUT'])
def update_actividad(id):
    data = request.get_json()
    actividad = Actividades.query.get_or_404(id)
    actividad.nombre = data['nombre']
    actividad.horas_totales = data['horas_totales']
    db.session.commit()
    return jsonify({'message': 'Actividad actualizada'})

@api.route('/actividades/<int:id>', methods=['DELETE'])
def delete_actividad(id):
    actividad = Actividades.query.get_or_404(id)
    db.session.delete(actividad)
    db.session.commit()
    return jsonify({'message': 'Actividad eliminada'})

# --------------------- ENDPOINTS DE ALUMNOS --------------------- #
@api.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = Alumnos.query.all()
    return jsonify([{
        'no_control': a.no_control,
        'nombre_completo': a.nombre_completo,
        'carrera': a.carrera,
        'semestre': a.semestre,
        'edad': a.edad,
        'creditos_complementarios': a.creditos_complementarios
    } for a in alumnos])

@api.route('/alumnos', methods=['POST'])
def create_alumno():
    data = request.get_json()
    new_alumno = Alumnos(
        no_control=data['no_control'],
        nombre_completo=data['nombre_completo'],
        carrera=data['carrera'],
        semestre=data['semestre'],
        edad=data['edad'],
        creditos_complementarios=data['creditos_complementarios']
    )
    db.session.add(new_alumno)
    db.session.commit()
    return jsonify({'message': 'Alumno creado', 'no_control': new_alumno.no_control}), 201

@api.route('/alumnos/<int:no_control>', methods=['PUT'])
def update_alumno(no_control):
    data = request.get_json()
    alumno = Alumnos.query.get_or_404(no_control)
    alumno.nombre_completo = data['nombre_completo']
    alumno.carrera = data['carrera']
    alumno.semestre = data['semestre']
    alumno.edad = data['edad']
    alumno.creditos_complementarios = data['creditos_complementarios']
    db.session.commit()
    return jsonify({'message': 'Alumno actualizado'})

@api.route('/alumnos/<int:no_control>', methods=['DELETE'])
def delete_alumno(no_control):
    alumno = Alumnos.query.get_or_404(no_control)
    db.session.delete(alumno)
    db.session.commit()
    return jsonify({'message': 'Alumno eliminado'})

# --------------------- ENDPOINTS DE MAESTROS --------------------- #
@api.route('/maestros', methods=['GET'])
def get_maestros():
    maestros = Maestros.query.all()
    return jsonify([{
        'no_control': m.no_control,
        'nombre_completo': m.nombre_completo,
        'actividad_id': m.actividad_id
    } for m in maestros])

@api.route('/maestros', methods=['POST'])
def create_maestro():
    data = request.get_json()
    new_maestro = Maestros(
        no_control=data['no_control'],
        nombre_completo=data['nombre_completo'],
        actividad_id=data['actividad_id']
    )
    db.session.add(new_maestro)
    db.session.commit()
    return jsonify({'message': 'Maestro creado', 'no_control': new_maestro.no_control}), 201

@api.route('/maestros/<int:no_control>', methods=['PUT'])
def update_maestro(no_control):
    data = request.get_json()
    maestro = Maestros.query.get_or_404(no_control)
    maestro.nombre_completo = data['nombre_completo']
    maestro.actividad_id = data['actividad_id']
    db.session.commit()
    return jsonify({'message': 'Maestro actualizado'})

@api.route('/maestros/<int:no_control>', methods=['DELETE'])
def delete_maestro(no_control):
    maestro = Maestros.query.get_or_404(no_control)
    db.session.delete(maestro)
    db.session.commit()
    return jsonify({'message': 'Maestro eliminado'})

# --------------------- ENDPOINTS DE EN CURSO --------------------- #
@api.route('/en_curso', methods=['GET'])
def get_en_curso():
    en_curso = EnCurso.query.all()
    return jsonify([{
        'id_curso': e.id_curso,
        'alumno_no_control': e.alumno_no_control,
        'maestro_no_control': e.maestro_no_control,
        'dia_semana': e.dia_semana,
        'horario': e.horario,
        'horas_llevadas': e.horas_llevadas,
        'horas_pendientes': e.horas_pendientes
    } for e in en_curso])

@api.route('/en_curso', methods=['POST'])
def create_en_curso():
    data = request.get_json()
    new_en_curso = EnCurso(
        alumno_no_control=data['alumno_no_control'],
        maestro_no_control=data['maestro_no_control'],
        dia_semana=data['dia_semana'],
        horario=data['horario'],
        horas_llevadas=data['horas_llevadas'],
        horas_pendientes=data['horas_pendientes']
    )
    db.session.add(new_en_curso)
    db.session.commit()
    return jsonify({'message': 'Curso creado', 'id_curso': new_en_curso.id_curso}), 201

@api.route('/en_curso/<int:id_curso>', methods=['PUT'])
def update_en_curso(id_curso):
    data = request.get_json()
    en_curso = EnCurso.query.get_or_404(id_curso)
    en_curso.alumno_no_control = data['alumno_no_control']
    en_curso.maestro_no_control = data['maestro_no_control']
    en_curso.dia_semana = data['dia_semana']
    en_curso.horario = data['horario']
    en_curso.horas_llevadas = data['horas_llevadas']
    en_curso.horas_pendientes = data['horas_pendientes']
    db.session.commit()
    return jsonify({'message': 'Curso actualizado'})

@api.route('/en_curso/<int:id_curso>', methods=['DELETE'])
def delete_en_curso(id_curso):
    en_curso = EnCurso.query.get_or_404(id_curso)
    db.session.delete(en_curso)
    db.session.commit()
    return jsonify({'message': 'Curso eliminado'})

# Registrando el Blueprint en la aplicación
app.register_blueprint(api, url_prefix='/api')

# Crear las tablas en la base de datos (solo si no existen)
with app.app_context():
    db.create_all()

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
