# services.py
from sqlalchemy.orm import Session
from models import Activity, Student, Teacher, InProgress
from sqlalchemy import func

# Servicios para Activity
def create_activity(db: Session, name: str, total_hours: int):
    new_activity = Activity(name=name, total_hours=total_hours)
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity

def get_activities(db: Session):
    return db.query(Activity).filter(Activity.deleted_at.is_(None)).all()

def update_activity(db: Session, activity_id: int, name: str = None, total_hours: int = None):
    activity = db.query(Activity).filter(Activity.activity_id == activity_id).first()
    if activity:
        if name:
            activity.name = name
        if total_hours:
            activity.total_hours = total_hours
        db.commit()
        db.refresh(activity)
    return activity

def delete_activity(db: Session, activity_id: int):
    activity = db.query(Activity).filter(Activity.activity_id == activity_id).first()
    if activity:
        activity.deleted_at = func.current_timestamp()
        db.commit()
    return activity

# Servicios para Student
def create_student(db: Session, student_id: int, full_name: str, major: str, semester: int, age: int, complementary_credits: int = 0):
    new_student = Student(
        student_id=student_id,
        full_name=full_name,
        major=major,
        semester=semester,
        age=age,
        complementary_credits=complementary_credits
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_students(db: Session):
    return db.query(Student).filter(Student.deleted_at.is_(None)).all()

def update_student(db: Session, student_id: int, full_name: str = None, major: str = None, semester: int = None, age: int = None, complementary_credits: int = None):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if student:
        if full_name:
            student.full_name = full_name
        if major:
            student.major = major
        if semester:
            student.semester = semester
        if age:
            student.age = age
        if complementary_credits is not None:
            student.complementary_credits = complementary_credits
        db.commit()
        db.refresh(student)
    return student

def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if student:
        student.deleted_at = func.current_timestamp()
        db.commit()
    return student

# Servicios para Teacher
def create_teacher(db: Session, teacher_id: int, full_name: str, activity_id: int):
    new_teacher = Teacher(
        teacher_id=teacher_id,
        full_name=full_name,
        activity_id=activity_id
    )
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def get_teachers(db: Session):
    return db.query(Teacher).filter(Teacher.deleted_at.is_(None)).all()

def update_teacher(db: Session, teacher_id: int, full_name: str = None, activity_id: int = None):
    teacher = db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    if teacher:
        if full_name:
            teacher.full_name = full_name
        if activity_id:
            teacher.activity_id = activity_id
        db.commit()
        db.refresh(teacher)
    return teacher

def delete_teacher(db: Session, teacher_id: int):
    teacher = db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    if teacher:
        teacher.deleted_at = func.current_timestamp()
        db.commit()
    return teacher

# Servicios para InProgress
def create_in_progress(db: Session, student_id: int, teacher_id: int, day_of_week: str, schedule: str, hours_completed: int, hours_pending: int):
    new_course = InProgress(
        student_id=student_id,
        teacher_id=teacher_id,
        day_of_week=day_of_week,
        schedule=schedule,
        hours_completed=hours_completed,
        hours_pending=hours_pending
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

def get_in_progress(db: Session):
    return db.query(InProgress).filter(InProgress.deleted_at.is_(None)).all()

def update_in_progress(db: Session, course_id: int, hours_completed: int = None, hours_pending: int = None):
    course = db.query(InProgress).filter(InProgress.course_id == course_id).first()
    if course:
        if hours_completed is not None:
            course.hours_completed = hours_completed
        if hours_pending is not None:
            course.hours_pending = hours_pending
        db.commit()
        db.refresh(course)
    return course

def delete_in_progress(db: Session, course_id: int):
    course = db.query(InProgress).filter(InProgress.course_id == course_id).first()
    if course:
        course.deleted_at = func.current_timestamp()
        db.commit()
    return course
