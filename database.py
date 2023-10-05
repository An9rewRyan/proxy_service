from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="1234",
    host="db",
    database="main_db"
)

engine = create_engine(url)

# Session = sessionmaker(bind=engine)
# session = Session()