from sqlalchemy.ext.declarative import declarative_base


# Base: class where all models will be registered, and this creates the metadata for all models
# later this metadata will be used to create all tables in the database
Base = declarative_base()