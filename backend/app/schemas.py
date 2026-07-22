# ==========================================================
#                    PYDANTIC SCHEMAS
# ==========================================================

# This file contains Pydantic models.
# These models validate API request and response data.

# ----------------------------------------------------------
# Import Required Modules
# ----------------------------------------------------------

from pydantic import BaseModel
from typing import Optional

# ----------------------------------------------------------
# Student Create Schema
# ----------------------------------------------------------

class StudentCreate(BaseModel):
    """
    Used when creating a new student.
    """

    name: str
    email: str
    course: str
    city: str
    phone: Optional[int] = None


# ----------------------------------------------------------
# Student Update Schema
# ----------------------------------------------------------

class StudentUpdate(BaseModel):
    """
    Used when updating an existing student.
    """
    # docstring ⬆️ - used for telling people/collaborators what the code/function/class does.

    name: str
    email: str
    course: str
    city: str
    phone: Optional[int] = None


# ----------------------------------------------------------
# Student Response Schema
# ----------------------------------------------------------

class StudentResponse(BaseModel):
    """
    Used when returning student data to the client.
    """

    id: int
    name: str
    email: str
    course: str
    city: str
    phone: Optional[int] = None

    # Allows Pydantic to convert SQLAlchemy model objects into JSON responses.

    model_config = {
        "from_attributes": True
    }