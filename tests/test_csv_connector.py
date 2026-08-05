from datasentinel.connectors.csv_connector import CSVConnector


def test_csv_connector():

    connector = CSVConnector(
        "tests/data/employees.csv"
    )

    connector.connect()

    dataframe = connector.load()

    connector.disconnect()

    assert dataframe is not None

    assert len(dataframe) > 0

    assert "id" in dataframe.columns

    assert "name" in dataframe.columns