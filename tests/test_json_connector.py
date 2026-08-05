from pathlib import Path

from datasentinel.connectors.json_connector import JSONConnector


def test_json_connector():

    json_path = Path("data/sample/employees.json")

    connector = JSONConnector(str(json_path))

    connector.connect()

    dataframe = connector.load()

    connector.disconnect()

    assert dataframe is not None
    assert not dataframe.empty

    assert "id" in dataframe.columns
    assert "name" in dataframe.columns