from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite database used for local development and demo
DATABASE_URL = "sqlite:///./aiops.db"


# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Create DB session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for all SQLAlchemy models
Base = declarative_base()


def get_db():
    """
    Provide database session to API routes.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()