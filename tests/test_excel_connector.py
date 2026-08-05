from pathlib import Path

from datasentinel.connectors.excel_connector import ExcelConnector


def test_excel_connector():

    excel_path = Path("data/sample/employees.xlsx")

    connector = ExcelConnector(str(excel_path))

    connector.connect()

    dataframe = connector.load()

    connector.disconnect()

    assert dataframe is not None
    assert not dataframe.empty

    assert "id" in dataframe.columns
    assert "name" in dataframe.columns