from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from models.base import Base

# step1: define database URL
DATABASE_URL = "sqlite:///./user.db" 
# postgresql://<user_name>:<password>@localhost:5432/<dbname>
# mysql://<username>:<password>@<host>:<port>/<database_name>
# <engine>:///<username>:<password>@<host>:<port>/<database_name>

# step2: create engine and session local
# create_engine: establish connection with database (act as a key to a door)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# sessionmaker: create session (act as a handle to open the door)
sessionLocal = sessionmaker(bind=engine)

# step3: create all tables
# Base: import from models.base where all models are registered
Base.metadata.create_all(bind=engine)

