import logging
from pathlib import Path

import pandas as pd


logger = logging.getLogger(__name__)


class JSONConnector:

    def __init__(self, file_path: str):

        self.file_path = file_path

    def connect(self):

        logger.info(f"Connecting to JSON file: {self.file_path}")

    def load(self):

        try:

            dataframe = pd.read_json(self.file_path)

            logger.info(
                f"Successfully loaded {len(dataframe)} rows."
            )

            return dataframe

        except FileNotFoundError:

            logger.error("JSON file not found.")
            raise

        except ValueError:

            logger.error("Invalid JSON file.")
            raise

    def disconnect(self):

        logger.info("Connection closed.")