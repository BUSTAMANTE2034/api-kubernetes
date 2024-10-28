from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

db = SQLAlchemy()  # Inicializa SQLAlchemy

class Actividad(db.Model):
    __tablename__ = 'Actividades'
    
    id_actividad = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    horas_totales = Column(Integer, nullable=False)

    # Relación con la tabla Maestros
    maestros = relationship("Maestro", back_populates="actividad")

class Alumno(db.Model):
    __tablename__ = 'Alumnos'

    no_control = Column(Integer, primary_key=True)
    nombre_completo = Column(String(100), nullable=False)
    carrera = Column(String(50), nullable=False)
    semestre = Column(Integer, nullable=False)
    edad = Column(Integer, nullable=False)
    creditos_complementarios = Column(Integer, default=0)

    # Relación con la tabla En_Curso
    cursos = relationship("EnCurso", back_populates="alumno")

class Maestro(db.Model):
    __tablename__ = 'Maestros'

    no_control = Column(Integer, primary_key=True)
    nombre_completo = Column(String(100), nullable=False)
    actividad_id = Column(Integer, ForeignKey('Actividades.id_actividad'), nullable=False)

    # Relación con la tabla Actividades
    actividad = relationship("Actividad", back_populates="maestros")
    
    # Relación con la tabla En_Curso
    cursos = relationship("EnCurso", back_populates="maestro")

class EnCurso(db.Model):
    __tablename__ = 'En_Curso'

    id_curso = Column(Integer, primary_key=True, autoincrement=True)
    alumno_no_control = Column(Integer, ForeignKey('Alumnos.no_control'), nullable=False)
    maestro_no_control = Column(Integer, ForeignKey('Maestros.no_control'), nullable=False)
    dia_semana = Column(String(20), nullable=False)
    horario = Column(String(50), nullable=False)  # Ejemplo: "10:00 - 13:00"
    horas_llevadas = Column(Integer, nullable=False)
    horas_pendientes = Column(Integer, nullable=False)

    # Relaciones
    alumno = relationship("Alumno", back_populates="cursos")
    maestro = relationship("Maestro", back_populates="cursos")
