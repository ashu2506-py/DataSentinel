from datasentinel.connectors.csv_connector import CSVConnector

connector = CSVConnector("data/sample/employees.csv")

connector.connect()

df = connector.load()

print(df.head())

connector.disconnect()