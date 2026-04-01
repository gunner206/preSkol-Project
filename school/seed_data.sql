-- Désactiver les contraintes de clés étrangères pour l'insertion
PRAGMA foreign_keys = OFF;

-- ==========================================
-- 0. NETTOYAGE (Pour éviter les erreurs UNIQUE constraint failed)
-- ==========================================
DELETE FROM faculty_result;
DELETE FROM faculty_holiday;
DELETE FROM faculty_exam;
DELETE FROM faculty_timetable;
DELETE FROM subject_subject;
DELETE FROM department_department;
DELETE FROM student_student;
DELETE FROM student_parent;
DELETE FROM teacher_teacher;
DELETE FROM home_auth_customuser;

-- ==========================================
-- 1. USERS (home_auth_customuser)
-- (Mot de passe à changer après insertion via 'python manage.py changepassword')
-- ==========================================
INSERT INTO home_auth_customuser (id, password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, is_authorized, is_student, is_admin, is_teacher)
VALUES 
(1, 'unhashed_password', 1, 'admin@school.com', 'Super', 'Admin', 'admin@school.com', 1, 1, '2026-04-01 10:00:00', 1, 0, 1, 0),
(2, 'unhashed_password', 0, 'teacher1@school.com', 'Alan', 'Turing', 'teacher1@school.com', 0, 1, '2026-04-01 10:00:00', 1, 0, 0, 1),
(3, 'unhashed_password', 0, 'teacher2@school.com', 'Marie', 'Curie', 'teacher2@school.com', 0, 1, '2026-04-01 10:00:00', 1, 0, 0, 1),
(4, 'unhashed_password', 0, 'student1@school.com', 'John', 'Smith', 'student1@school.com', 0, 1, '2026-04-01 10:00:00', 1, 1, 0, 0),
(5, 'unhashed_password', 0, 'student2@school.com', 'Sophie', 'Martin', 'student2@school.com', 0, 1, '2026-04-01 10:00:00', 1, 1, 0, 0);

-- ==========================================
-- 2. TEACHERS (teacher_teacher)
-- (Ajout du champ 'experience' qui manquait)
-- ==========================================
INSERT INTO teacher_teacher (id, first_name, last_name, teacher_id, gender, date_of_birth, mobile_number, joining_date, experience, teacher_image, user_id)
VALUES 
(1, 'Alan', 'Turing', 'T-001', 'Male', '1985-06-23', '+212600000001', '2020-09-01', '5 Years', '', 2),
(2, 'Marie', 'Curie', 'T-002', 'Female', '1990-11-07', '+212600000002', '2021-09-01', '8 Years', '', 3);

-- ==========================================
-- 3. PARENTS (student_parent)
-- (1 parent distinct par étudiant pour respecter la contrainte Unique/OneToOne)
-- ==========================================
INSERT INTO student_parent (id, father_name, father_occupation, father_mobile, father_email, mother_name, mother_occupation, mother_mobile, mother_email, present_address, permanent_address)
VALUES 
(1, 'Robert Smith', 'Engineer', '+212611111111', 'robert.smith@email.com', 'Sarah Smith', 'Doctor', '+212622222222', 'sarah.smith@email.com', '123 Main Street', '123 Main Street'),
(2, 'Jean Martin', 'Architect', '+212688888888', 'jean.martin@email.com', 'Claire Martin', 'Teacher', '+212699999999', 'claire.martin@email.com', '456 Avenue', '456 Avenue');

-- ==========================================
-- 4. STUDENTS (student_student)
-- (Retrait de 'user_id' qui n'est pas dans votre modèle)
-- ==========================================
INSERT INTO student_student (id, first_name, last_name, student_id, gender, date_of_birth, student_class, joining_date, mobile_number, admission_number, section, student_image, parent_id)
VALUES 
(1, 'John', 'Smith', 'S-1001', 'Male', '2010-05-14', 'Class 10 A', '2025-09-01', '+212633333333', 'ADM-2025-01', 'A', '', 1),
(2, 'Sophie', 'Martin', 'S-1002', 'Female', '2010-08-20', 'Class 10 A', '2025-09-01', '+212644444444', 'ADM-2025-02', 'A', '', 2);

-- ==========================================
-- 5. DEPARTMENTS (department_department)
-- (Retrait de 'head_of_department_id')
-- ==========================================
INSERT INTO department_department (id, name, description)
VALUES 
(1, 'Mathematics', 'Department of Advanced and Basic Mathematics'),
(2, 'Science', 'Department of Physics, Chemistry, and Biology');

-- ==========================================
-- 6. SUBJECTS (subject_subject)
-- ==========================================
INSERT INTO subject_subject (id, name, description, department_id, teacher_id)
VALUES 
(1, 'Algebra', 'Advanced Algebra', 1, 1),
(2, 'Physics', 'Mechanics and Thermodynamics', 2, 2);

-- ==========================================
-- 7. TIME TABLE (faculty_timetable)
-- ==========================================
INSERT INTO faculty_timetable (id, class_name, subject, date, start_time, end_time, teacher_id)
VALUES 
(1, 'Class 10 A', 'Algebra', '2026-04-06', '08:00:00', '10:00:00', 1),
(2, 'Class 10 A', 'Physics', '2026-04-06', '10:30:00', '12:30:00', 2);

-- ==========================================
-- 8. EXAMS (faculty_exam)
-- ==========================================
INSERT INTO faculty_exam (id, name, exam_class, subject, exam_date, start_time, end_time)
VALUES 
(1, 'Mid-Term Math', 'Class 10 A', 'Algebra', '2026-05-15', '09:00:00', '11:00:00'),
(2, 'Mid-Term Physics', 'Class 10 A', 'Physics', '2026-05-16', '09:00:00', '11:00:00');

-- ==========================================
-- 9. RESULTS / NOTES (faculty_result)
-- ==========================================
INSERT INTO faculty_result (id, marks, comments, exam_id, student_id)
VALUES 
(1, 15.5, 'Très bon travail', 1, 1),
(2, 18.0, 'Excellent', 1, 2),
(3, 12.0, 'Peut mieux faire', 2, 1);

-- ==========================================
-- 10. HOLIDAYS (faculty_holiday)
-- ==========================================
INSERT INTO faculty_holiday (id, name, holiday_type, start_date, end_date, description)
VALUES 
(1, 'Spring Break', 'Term Break', '2026-04-20', '2026-04-26', 'One week break for the Spring semester.'),
(2, 'Labor Day', 'Public Holiday', '2026-05-01', '2026-05-01', 'National holiday.');

-- Réactiver les clés étrangères
PRAGMA foreign_keys = ON;