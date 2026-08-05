from datasentinel.connectors.factory import ConnectorFactory
import os

print("Current Working Directory:", os.getcwd())
print("File Exists:", os.path.exists("data/sample/employees.xlsx"))
connector = ConnectorFactory.create(
    "excel",
    "data/sample/employees.xlsx"
)

connector.connect()

df = connector.load()

print(df)

connector.disconnect()