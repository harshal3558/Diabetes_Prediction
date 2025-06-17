from src.dp.logger import logging
from src.dp.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info('The execution has started')

    try:
        a=1/10
    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e,sys)