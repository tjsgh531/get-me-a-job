from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a connection to the database
DB_URL = "postgresql://postgres:wldnjs5768@localhost:5432/getmeajob_review"
engine = create_engine(DB_URL)
session = sessionmaker(bind=engine)
Base = declarative_base()

