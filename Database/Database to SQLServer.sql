
-- Crear base de datos
CREATE DATABASE Act;  -- Actividades Complementarias
USE Act;

-- Crear tabla de Actividades
CREATE TABLE Activities (
    activity_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(50) NOT NULL,
    total_hours INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL
);

-- Crear trigger para actualizar 'updated_at' al modificar la fila
CREATE TRIGGER trg_UpdateActivities
ON Activities
AFTER UPDATE
AS
BEGIN
    UPDATE Activities
    SET updated_at = CURRENT_TIMESTAMP
    WHERE activity_id IN (SELECT activity_id FROM inserted);
END;

-- Crear tabla de Estudiantes
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    major VARCHAR(50) NOT NULL,
    semester INT NOT NULL,
    age INT NOT NULL,
    complementary_credits INT DEFAULT 0 CHECK (complementary_credits BETWEEN 0 AND 5),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL
);

-- Crear trigger para actualizar 'updated_at' al modificar la fila en Students
CREATE TRIGGER trg_UpdateStudents
ON Students
AFTER UPDATE
AS
BEGIN
    UPDATE Students
    SET updated_at = CURRENT_TIMESTAMP
    WHERE student_id IN (SELECT student_id FROM inserted);
END;

-- Crear tabla de Maestros
CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    activity_id INT NOT NULL,
    FOREIGN KEY (activity_id) REFERENCES Activities(activity_id),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL
);

-- Crear trigger para actualizar 'updated_at' al modificar la fila en Teachers
CREATE TRIGGER trg_UpdateTeachers
ON Teachers
AFTER UPDATE
AS
BEGIN
    UPDATE Teachers
    SET updated_at = CURRENT_TIMESTAMP
    WHERE teacher_id IN (SELECT teacher_id FROM inserted);
END;

-- Crear tabla En Curso
CREATE TABLE In_Progress (
    course_id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT NOT NULL,
    teacher_id INT NOT NULL,
    day_of_week VARCHAR(20) NOT NULL,
    schedule VARCHAR(50) NOT NULL,  -- Ejemplo: "10:00 - 13:00"
    hours_completed INT NOT NULL,
    hours_pending INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL
);

-- Crear trigger para actualizar 'updated_at' al modificar la fila en In_Progress
CREATE TRIGGER trg_UpdateInProgress
ON In_Progress
AFTER UPDATE
AS
BEGIN
    UPDATE In_Progress
    SET updated_at = CURRENT_TIMESTAMP
    WHERE course_id IN (SELECT course_id FROM inserted);
END;
