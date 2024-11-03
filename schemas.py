# schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Activity Schemas
class ActivityCreateSchema(BaseModel):
    name: str
    total_hours: int

class ActivityUpdateSchema(BaseModel):
    name: Optional[str] = None
    total_hours: Optional[int] = None

class ActivitySchema(ActivityCreateSchema):
    activity_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# Student Schemas
class StudentCreateSchema(BaseModel):
    student_id: int
    full_name: str
    major: str
    semester: int
    age: int
    complementary_credits: Optional[int] = 0

class StudentUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    major: Optional[str] = None
    semester: Optional[int] = None
    age: Optional[int] = None
    complementary_credits: Optional[int] = None

class StudentSchema(StudentCreateSchema):
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# Teacher Schemas
class TeacherCreateSchema(BaseModel):
    teacher_id: int
    full_name: str
    activity_id: int

class TeacherUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    activity_id: Optional[int] = None

class TeacherSchema(TeacherCreateSchema):
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# InProgress Schemas
class InProgressCreateSchema(BaseModel):
    student_id: int
    teacher_id: int
    day_of_week: str
    schedule: str
    hours_completed: int
    hours_pending: int

class InProgressUpdateSchema(BaseModel):
    hours_completed: Optional[int] = None
    hours_pending: Optional[int] = None

class InProgressSchema(InProgressCreateSchema):
    course_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True
