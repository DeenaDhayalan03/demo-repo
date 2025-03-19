import logging
from scripts.constants.app_constants import AppConstants

logging.basicConfig(
    filename="logs/EPR.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def get_logger():
    return logging.getLogger()

logger = logging.getLogger("employees_db")

def log_employee_creation():
    logger.info(AppConstants.EMPLOYEE_CREATED)

def log_employee_update():
    logger.info(AppConstants.EMPLOYEE_UPDATED)

def log_employee_deletion():
    logger.info(AppConstants.EMPLOYEE_DELETED)

def log_manager_access():
    logger.info(AppConstants.MANAGER_VIEW_SUCCESS)

def log_admin_access():
    logger.info(AppConstants.ADMIN_MANAGE_EMPLOYEES)

