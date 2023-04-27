from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from sqlalchemy.exc import OperationalError

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# try:

#     with engine.connect() as connection:
#         connection.execute('SELECT 1')

#         #connection successful
#         print('Database connection successful!')
# except OperationalError as e:
#     print('Database connection failed:', e)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)