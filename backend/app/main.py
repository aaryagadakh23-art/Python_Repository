# ==========================================================
#                     FASTAPI APPLICATION
# ==========================================================

# This is the main file of our FastAPI project.
# It creates the FastAPI app and defines all API endpoints.

# ----------------------------------------------------------
# Import Required Modules
# ----------------------------------------------------------

from fastapi import FastAPI, Depends, HTTPException 

from sqlalchemy.orm import Session

from app.database import engine, Base, get_db

from app import models, schemas, crud

from app.logger import logger
from app.config import APP_NAME
from app.config import APP_VERSION

from fastapi.middleware.cors import CORSMiddleware

# ----------------------------------------------------------
# Create Database Tables
# ----------------------------------------------------------

# This line creates all tables that inherit from Base.
# If the table already exists, nothing happens. 

Base.metadata.create_all(bind=engine) 

logger.info("Database Tables Checked/Created.")

# ----------------------------------------------------------
# Create FastAPI App
# ----------------------------------------------------------

app = FastAPI(

    title=APP_NAME,

    version=APP_VERSION

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("FastAPI Application Started.")

logger.info("CORS Enabled.")

# ==========================================================
# HOME API
# ==========================================================

@app.get("/")

def home():

    logger.info("Home API Called.")

    return {

        "message": "Welcome to Student Management API"

    }

# ==========================================================
# CREATE STUDENT
# ==========================================================

@app.post(

    "/students",

    response_model=schemas.StudentResponse 

)

def create_student(

    student: schemas.StudentCreate,

    db: Session = Depends(get_db)

):

    logger.info("Create Student API Called.")

    return crud.create_student(

        db,

        student

    )

# ==========================================================
# GET ALL STUDENTS
# ==========================================================

@app.get(

    "/students",

    response_model=list[schemas.StudentResponse]

)

def get_students(

    db: Session = Depends(get_db)

):

    logger.info("Get All Students API Called.")

    return crud.get_students(db)

# ==========================================================
# GET STUDENT BY ID
# ==========================================================

@app.get(

    "/students/{student_id}",

    response_model=schemas.StudentResponse

)

def get_student(

    student_id: int,

    db: Session = Depends(get_db)

):

    student = crud.get_student_by_id(

        db,

        student_id

    )

    if student is None:

        logger.warning("Student Not Found.")

        raise HTTPException(

            status_code=404,

            detail="Student Not Found"

        )

    return student

# ==========================================================
# UPDATE STUDENT
# ==========================================================

@app.put(

    "/students/{student_id}",

    response_model=schemas.StudentResponse

)

def update_student(

    student_id: int,

    updated_student: schemas.StudentUpdate,

    db: Session = Depends(get_db)

):

    student = crud.update_student(

        db,

        student_id,

        updated_student

    )

    if student is None:

        raise HTTPException(

            status_code=404,

            detail="Student Not Found"

        )

    return student

# ==========================================================
# DELETE STUDENT
# ==========================================================

@app.delete(

    "/students/{student_id}"

)

def delete_student(

    student_id: int,

    db: Session = Depends(get_db)

):

    student = crud.delete_student(

        db,

        student_id

    )

    if student is None:

        raise HTTPException(

            status_code=404,

            detail="Student Not Found"

        )

    logger.info(f"Student Deleted : {student.name}")
    
    return {

        "message": "Student Deleted Successfully"

    }