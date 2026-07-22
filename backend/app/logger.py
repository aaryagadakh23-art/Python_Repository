# ==========================================================
#                     LOGGER CONFIGURATION
# ==========================================================

# This file configures logging for the entire application.
# It also creates the logs folder automatically if it
# doesn't already exist.

# ----------------------------------------------------------
# Import Required Modules
# ----------------------------------------------------------

import logging
import os

from app.config import LOG_FILE, LOG_LEVEL

# ----------------------------------------------------------
# Create Logs Folder
# ----------------------------------------------------------

# Extract the folder name from LOG_FILE.
# Example:
#
# logs/app.log
#
# becomes
#
# logs

log_folder = os.path.dirname(LOG_FILE)

# log_folder = logs

# Check whether the folder exists.

if not os.path.exists(log_folder):

    os.makedirs(log_folder)

    print("Logs folder created.")

else:

    print("Logs folder already exists.")

# ----------------------------------------------------------
# Configure Logging
# ----------------------------------------------------------

logging.basicConfig(

    filename=LOG_FILE,

    level=getattr(logging, LOG_LEVEL.upper()),

    format="%(asctime)s | %(levelname)s | %(message)s"

)

# ----------------------------------------------------------
# Create Logger Object
# ----------------------------------------------------------

logger = logging.getLogger(__name__)

# ----------------------------------------------------------
# Application Started
# ----------------------------------------------------------

logger.info("Logger initialized successfully.")