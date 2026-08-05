from typing import Any

from datasentinel.connectors.base import BaseConnector
from datasentinel.connectors.csv_connector import CSVConnector
from datasentinel.connectors.excel_connector import ExcelConnector


class ConnectorFactory:
    """
    Factory class responsible for creating connector instances.
    """

    _connectors = {
        "csv": CSVConnector,
        "excel":ExcelConnector,
    }

    @classmethod
    def create(cls, connector_type: str, *args: Any, **kwargs: Any) -> BaseConnector:
        connector_type = connector_type.lower()

        if connector_type not in cls._connectors:
            raise ValueError(
                f"Unsupported connector type: {connector_type}"
            )

        connector_class = cls._connectors[connector_type]

        return connector_class(*args, **kwargs)

    @classmethod
    def register(cls, connector_type: str, connector_class):
        cls._connectors[connector_type.lower()] = connector_class

    @classmethod
    def available_connectors(cls):
        return list(cls._connectors.keys())