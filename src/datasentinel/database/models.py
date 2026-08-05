from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import JSON

from datetime import datetime

from datasentinel.database.database import Base


class ValidationRun(Base):

    __tablename__ = "validation_runs"

    id = Column(Integer, primary_key=True)

    dataset = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    validation = Column(JSON)

    schema = Column(JSON)

    anomaly = Column(JSON)

    html_report = Column(String)

    pdf_report = Column(String)