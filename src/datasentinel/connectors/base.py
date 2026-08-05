from abc import ABC, abstractmethod
import pandas as pd


class BaseConnector(ABC):
    """
    Abstract base class for all data connectors.
    """

    @abstractmethod
    def connect(self) -> None:
        """Establish connection to the data source."""
        pass

    @abstractmethod
    def load(self) -> pd.DataFrame:
        """Load data into a Pandas DataFrame."""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Close the connection."""
        pass