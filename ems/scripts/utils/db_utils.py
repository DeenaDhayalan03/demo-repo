import psycopg2
from scripts.constants.app_configuration import AppConfig
from scripts.constants.app_constants import AppConstants
from scripts.logging.logger import logger


def get_db_connection():
    logger.info('Entered into get_db_connection')
    logger.info(f"""host:{AppConfig.DATABASE_HOST},
            port={AppConfig.DATABASE_PORT},
            user={AppConfig.DATABASE_USER},
            password={AppConfig.DATABASE_PASSWORD},
            database={AppConfig.DATABASE_NAME}""")
    try:
        conn = psycopg2.connect(
            host=AppConfig.DATABASE_HOST,
            port=AppConfig.DATABASE_PORT,
            user=AppConfig.DATABASE_USER,
            password=AppConfig.DATABASE_PASSWORD,
            database=AppConfig.DATABASE_NAME
        )
        return conn
    except Exception as e:
        raise Exception(AppConstants.DATABASE_ERROR)
