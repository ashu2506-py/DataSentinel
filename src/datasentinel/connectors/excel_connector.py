import pandas as pd

from pandas.errors import EmptyDataError

from datasentinel.connectors.base import BaseConnector
from datasentinel.utils.logger import get_logger

logger = get_logger(__name__)


class ExcelConnector(BaseConnector):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def connect(self) -> None:
        logger.info(f"Connecting to Excel file: {self.file_path}")

    def load(self) -> pd.DataFrame:
        try:
            dataframe = pd.read_excel(self.file_path)

            logger.info(
                f"Successfully loaded {len(dataframe)} rows."
            )

            return dataframe

        except FileNotFoundError:
            logger.error("Excel file not found.")
            raise

        except EmptyDataError:
            logger.error("Excel file is empty.")
            raise

        except Exception as error:
            logger.exception(error)
            raise

    def disconnect(self) -> None:
        logger.info("Connection closed.")