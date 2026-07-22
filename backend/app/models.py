# ==========================================================
#                     DATABASE MODELS
# ==========================================================

# This file contains all the database tables.
# Every table is represented as a Python class.

# ----------------------------------------------------------
# Import Required Modules
# ----------------------------------------------------------

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base
# import uuid

# ----------------------------------------------------------
# Student Table
# ----------------------------------------------------------

class Student(Base):

    """
    Represents the 'students' table inside PostgreSQL.
    """

    # ------------------------------------------------------
    # Table Name
    # ------------------------------------------------------

    __tablename__ = "students"

    # ------------------------------------------------------
    # Columns
    # ------------------------------------------------------

    # Primary Key
    id = Column(
        Integer,
        primary_key=True,
        index=True 
    )

    # Student Name
    name = Column(
        String(100),
        nullable=False
        # unique=True
    )

    # Email Address
    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    # Course Name
    course = Column(
        String(50),
        nullable=False
    )

    # City
    city = Column(
        String(50),
        nullable=False
    )

    # Phone Number
    phone = Column(
        Integer(),
        nullable=True
    )