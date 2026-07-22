# ==========================================================
#                    CRUD OPERATIONS
# ==========================================================

# This file contains all database operations.

# ----------------------------------------------------------
# Import Required Modules
# ----------------------------------------------------------

from sqlalchemy.orm import Session 

from app import models
from app import schemas

from app.logger import logger

# ==========================================================
# CREATE STUDENT
# ==========================================================

def create_student( 
    db: Session,
    student: schemas.StudentCreate 
):

    logger.info("Creating Student")

    db_student = models.Student(

        name=student.name,

        email=student.email,

        course=student.course,

        city=student.city,

        phone=student.phone

    )

    db.add(db_student)

    db.commit()

    db.refresh(db_student) 

    logger.info(f"Student Created : {db_student.name}")

    return db_student 

# Tasks to be Performed:

# Task 1:

# If student is created but not commmitted to the database, for that, write a logging message using conditional statements.

# If student is not created, then write a log message (level = warning).

# Phone number validation while making model/schema. What other data type should be used instead of String & Integer?


# ==========================================================
# GET ALL STUDENTS
# ==========================================================

def get_students(db: Session):

    logger.info("Fetching All Students...")

    return db.query(models.Student).all()

# ==========================================================
# GET STUDENT BY ID
# ==========================================================

def get_student_by_id(
    db: Session,
    student_id: int
):

    logger.info(f"Fetching Student ID : {student_id}...")

    return (

        db.query(models.Student).filter(models.Student.id == student_id).first()

    )


# ==========================================================
# UPDATE STUDENT
# ==========================================================

def update_student(
    db: Session,
    student_id: int,
    updated_student: schemas.StudentUpdate
):

    student = (

        db.query(models.Student)

        .filter(models.Student.id == student_id)

        .first()

    )

    if student is None:

        logger.warning("Student Not Found")

        return None
    else:
        student.name = updated_student.name

        student.email = updated_student.email

        student.course = updated_student.course

        student.city = updated_student.city

        student.phone = updated_student.phone

    db.commit()

    db.refresh(student)

    logger.info(f"Student Updated : {student.name}")

    return student


# ==========================================================
# DELETE STUDENT
# ==========================================================

def delete_student(
    db: Session,
    student_id: int
):

    student = (

        db.query(models.Student)

        .filter(models.Student.id == student_id)

        .first()

    )

    if student is None:

        logger.warning("Student Not Found")

        return None
    
    else:
        
        db.delete(student)
        
        # db.commit()

    db.commit()

    logger.info(f"Student Deleted : {student.name}")

    return student 

# Task 2:

# Check both if,else conditions in delete_student & update_student function is correct or not.