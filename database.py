from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///dabbawala.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    """Provide a new database session."""
    with Session(engine) as session:
        yield session