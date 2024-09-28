from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "mysql+pymysql://daniel_rl:appinit9@127.0.0.1:3306/appinit"


engine = create_engine(DATABASE_URL, echo=True)


Base = declarative_base()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
"""