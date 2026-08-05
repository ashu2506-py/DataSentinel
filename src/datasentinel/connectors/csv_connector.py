import pandas as pd

from pandas.errors import EmptyDataError, ParserError

from .base import BaseConnector
from datasentinel.utils.logger import get_logger


logger = get_logger(__name__)


class CSVConnector(BaseConnector):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def connect(self) -> None:
        logger.info(f"Connecting to {self.file_path}")

    def load(self) -> pd.DataFrame:

        try:
            dataframe = pd.read_csv(self.file_path)

            logger.info(
                f"Successfully loaded {len(dataframe)} rows."
            )

            return dataframe

        except FileNotFoundError:
            logger.error("CSV file not found.")
            raise

        except EmptyDataError:
            logger.error("CSV file is empty.")
            raise

        except ParserError:
            logger.error("Invalid CSV format.")
            raise

        except Exception as error:
            logger.exception(error)
            raise

    def disconnect(self) -> None:
        logger.info("Connection closed.")