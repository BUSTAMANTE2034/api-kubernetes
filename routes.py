# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config import SessionLocal
from services import (
    create_activity, get_activities, update_activity, delete_activity,
    create_student, get_students, update_student, delete_student,
    create_teacher, get_teachers, update_teacher, delete_teacher,
    create_in_progress, get_in_progress, update_in_progress, delete_in_progress
)
from schemas import (
    ActivitySchema, ActivityCreateSchema, ActivityUpdateSchema,
    StudentSchema, StudentCreateSchema, StudentUpdateSchema,
    TeacherSchema, TeacherCreateSchema, TeacherUpdateSchema,
    InProgressSchema, InProgressCreateSchema, InProgressUpdateSchema
)
from typing import List

router = APIRouter()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas para Activity
@router.get("/activities/", response_model=List[ActivitySchema])
def list_activities(db: Session = Depends(get_db)):
    return get_activities(db)

@router.post("/activities/", response_model=ActivitySchema)
def add_activity(activity: ActivityCreateSchema, db: Session = Depends(get_db)):
    return create_activity(db, activity.name, activity.total_hours)

@router.put("/activities/{activity_id}", response_model=ActivitySchema)
def modify_activity(activity_id: int, activity_data: ActivityUpdateSchema, db: Session = Depends(get_db)):
    activity = update_activity(db, activity_id, activity_data.name, activity_data.total_hours)
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity

@router.delete("/activities/{activity_id}")
def remove_activity(activity_id: int, db: Session = Depends(get_db)):
    activity = delete_activity(db, activity_id)
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return {"detail": "Activity deleted"}

# Rutas para Student
@router.get("/students/", response_model=List[StudentSchema])
def list_students(db: Session = Depends(get_db)):
    return get_students(db)

@router.post("/students/", response_model=StudentSchema)
def add_student(student: StudentCreateSchema, db: Session = Depends(get_db)):
    return create_student(
        db,
        student.student_id,
        student.full_name,
        student.major,
        student.semester,
        student.age,
        student.complementary_credits
    )

@router.put("/students/{student_id}", response_model=StudentSchema)
def modify_student(student_id: int, student_data: StudentUpdateSchema, db: Session = Depends(get_db)):
    student = update_student(
        db,
        student_id,
        student_data.full_name,
        student_data.major,
        student_data.semester,
        student_data.age,
        student_data.complementary_credits
    )
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.delete("/students/{student_id}")
def remove_student(student_id: int, db: Session = Depends(get_db)):
    student = delete_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted"}

# Rutas para Teacher
@router.get("/teachers/", response_model=List[TeacherSchema])
def list_teachers(db: Session = Depends(get_db)):
    return get_teachers(db)

@router.post("/teachers/", response_model=TeacherSchema)
def add_teacher(teacher: TeacherCreateSchema, db: Session = Depends(get_db)):
    return create_teacher(db, teacher.teacher_id, teacher.full_name, teacher.activity_id)

@router.put("/teachers/{teacher_id}", response_model=TeacherSchema)
def modify_teacher(teacher_id: int, teacher_data: TeacherUpdateSchema, db: Session = Depends(get_db)):
    teacher = update_teacher(db, teacher_id, teacher_data.full_name, teacher_data.activity_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.delete("/teachers/{teacher_id}")
def remove_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = delete_teacher(db, teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"detail": "Teacher deleted"}

# Rutas para InProgress
@router.get("/in_progress/", response_model=List[InProgressSchema])
def list_in_progress(db: Session = Depends(get_db)):
    return get_in_progress(db)

@router.post("/in_progress/", response_model=InProgressSchema)
def add_in_progress(in_progress: InProgressCreateSchema, db: Session = Depends(get_db)):
    return create_in_progress(
        db,
        in_progress.student_id,
        in_progress.teacher_id,
        in_progress.day_of_week,
        in_progress.schedule,
        in_progress.hours_completed,
        in_progress.hours_pending
    )

@router.put("/in_progress/{course_id}", response_model=InProgressSchema)
def modify_in_progress(course_id: int, in_progress_data: InProgressUpdateSchema, db: Session = Depends(get_db)):
    in_progress = update_in_progress(db, course_id, in_progress_data.hours_completed, in_progress_data.hours_pending)
    if in_progress is None:
        raise HTTPException(status_code=404, detail="InProgress not found")
    return in_progress

@router.delete("/in_progress/{course_id}")
def remove_in_progress(course_id: int, db: Session = Depends(get_db)):
    in_progress = delete_in_progress(db, course_id)
    if in_progress is None:
        raise HTTPException(status_code=404, detail="InProgress not found")
    return {"detail": "InProgress deleted"}
