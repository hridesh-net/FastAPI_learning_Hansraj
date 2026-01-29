from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from models.base import Base

# step1: define database URL
DATABASE_URL = "sqlite:///./user.db" 
# postgresql://<user_name>:<password>@localhost:5432/<dbname>
# mysql://<username>:<password>@<host>:<port>/<database_name>
# <engine>:///<username>:<password>@<host>:<port>/<database_name>

# step2: create engine and session local
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

