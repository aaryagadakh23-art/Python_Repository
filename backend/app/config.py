# ==========================================================
#                    CONFIGURATION FILE
# ==========================================================

# This file loads all environment variables from the .env file.
# Other files will import values from here instead of reading
# the .env file again and again.

# ----------------------------------------------------------
# Import Required Modules
# ----------------------------------------------------------

import os
from dotenv import load_dotenv

# ----------------------------------------------------------
# Load the .env File
# ----------------------------------------------------------

# Reads all variables from the .env file.
# After this line, we can use os.getenv().

load_dotenv()

# ----------------------------------------------------------
# Database Configuration
# ----------------------------------------------------------

# Reads the database host.

DB_HOST = os.getenv("DB_HOST")

# Reads the database port.

DB_PORT = os.getenv("DB_PORT")

# Reads the database name.

DB_NAME = os.getenv("DB_NAME")

# Reads the database username.

DB_USER = os.getenv("DB_USER")

# Reads the database password.

DB_PASSWORD = os.getenv("DB_PASSWORD")

# ----------------------------------------------------------
# Application Configuration
# ----------------------------------------------------------

APP_NAME = os.getenv("APP_NAME")

APP_VERSION = os.getenv("APP_VERSION")

DEBUG = os.getenv("DEBUG")

# ----------------------------------------------------------
# Logging Configuration
# ----------------------------------------------------------

LOG_LEVEL = os.getenv("LOG_LEVEL")

LOG_FILE = os.getenv("LOG_FILE")

# ----------------------------------------------------------
# SQLAlchemy Database URL
# ----------------------------------------------------------

# SQLAlchemy requires a single database URL.
# We create it by combining all database information.

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}" 
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ----------------------------------------------------------
# Display Configuration (For Learning Only)
# ----------------------------------------------------------
# In real-world projects, NEVER print passwords.
# This is only for students to understand how values
# are loaded from the .env file.

if __name__ == "__main__":


    # print("Application Name :", APP_NAME)

    # print("Version          :", APP_VERSION)

    # print("Database Host    :", DB_HOST)

    # print("Database Name    :", DB_NAME)

    # print("Database User    :", DB_USER)

    # print("Debug Mode       :", DEBUG)

    print()

    # print("Database URL")

    # print(DATABASE_URL)