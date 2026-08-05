from datasentinel.database.database import Base
from datasentinel.database.database import engine

from datasentinel.database import models

Base.metadata.create_all(engine)

print("Database Created Successfully")