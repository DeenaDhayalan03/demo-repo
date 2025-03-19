import logging
from fastapi import HTTPException, status

from scripts.constants.app_constants import AppConstants
from scripts.utils.db_queries import *

logger = logging.getLogger("employee_api")

class employee_handler:

 @staticmethod
 def create_employee(email: str, name: str, dept_id: int, role_id: int):
    try:
        employee = create_employee_query(email, name, dept_id, role_id)
        if employee:
            employee_id = execute_query(f"SELECT employee_id FROM employees WHERE employees.email = '{email}';", fetch_one=True)[0]

            logger.info(f" Employee Created: ID={employee_id}, Name={name}, Dept={dept_id}, Role={role_id}")
            return employee_id
        else:
            logger.error(" Employee creation failed.")
            return None
    except Exception as e:
        if 'employees_email_key' in str(e):
            logger.error(f"Employee with email: {email} already exists.")
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Employee with email: {email} already exists.")
        logger.error(f" Error creating employee: {e}")
        return None

 @staticmethod
 def read_employee(employee_id: int):
    try:
        employee = read_employee_query(employee_id)
        if employee:
            return employee
        logger.warning(f" Employee Not Found: ID={employee_id}")
        return None
    except Exception as e:
        logger.error(f" Error fetching employee: {e}")
        return None

 @staticmethod
 def read_employee_by_department(employee_id: int, dept_id: int):
    try:
        employee = read_employee_query_by_department(employee_id, dept_id)
        if employee:
            return employee
        logger.warning(f" Employee Not Found in Dept: ID={employee_id}, Dept ID={dept_id}")
        return None
    except Exception as e:
        logger.error(f" Error fetching employee by department: {e}")
        return None

 @staticmethod
 def update_employee(employee_id: int, email: str, name: str, dept_id: int, role_id: int):
    try:
        employee = read_employee_query(employee_id)
        if not employee:
            logger.warning(f" Employee Not Found for Update: ID={employee_id}")
            return None

        update_employee_query(employee_id, email, name, dept_id, role_id)
        logger.info(f" Employee Updated: ID={employee_id}")
        return AppConstants.UPDATE_SUCCESS

    except Exception as e:
        logger.error(f"Error updating employee: {e}")
        return None

 @staticmethod
 def delete_employee(employee_id: int):
    try:
        employee = read_employee_query(employee_id)
        if not employee:
            logger.warning(f" Employee Not Found for Deletion: ID={employee_id}")
            return None

        delete_employee_query(employee_id)
        logger.info(f" Employee Deleted: ID={employee_id}")
        return AppConstants.DELETE_SUCCESS

    except Exception as e:
        logger.error(f" Error deleting employee: {e}")
        return None
