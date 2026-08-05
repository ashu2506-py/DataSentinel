from datasentinel.connectors.factory import ConnectorFactory


connector = ConnectorFactory.create(
    "csv",
    "data/sample/employees.csv"
)

connector.connect()

df = connector.load()

print(df)

connector.disconnect()