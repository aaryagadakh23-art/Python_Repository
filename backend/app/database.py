# ==========================================================
#                    DATABASE CONFIGURATION
# ==========================================================

# This file connects our FastAPI application to PostgreSQL
# using SQLAlchemy.

# ----------------------------------------------------------
# Import Required Modules
# ----------------------------------------------------------

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from app.config import DATABASE_URL 

from app.logger import logger

# ----------------------------------------------------------
# Create Database Engine
# ----------------------------------------------------------

# The engine knows how to communicate with PostgreSQL.

engine = create_engine(

    DATABASE_URL,

    echo=True

)

# echo=True prints SQL queries in the terminal.
# This is useful while learning.
# In production, we usually keep it False.

logger.info("Database Engine Created Successfully.")

# ----------------------------------------------------------
# Create Session Factory
# ----------------------------------------------------------

# SessionLocal creates new database sessions.
# Every API request will use a new session.

SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)

logger.info("Session Factory Created.")

# ----------------------------------------------------------
# Base Class
# ----------------------------------------------------------

# Every SQLAlchemy model will inherit from Base.

Base = declarative_base()

logger.info("Base Class Created.")

# ----------------------------------------------------------
# Dependency Function
# ----------------------------------------------------------

# This function creates a database session,
# gives it to the API,
# and closes it automatically.

def get_db():

    db = SessionLocal() 

    try:

        logger.info("Database Session Started...")

        yield db 

    finally:

        db.close() 

        logger.info("Database Session Closed.") 