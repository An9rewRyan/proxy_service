from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="1234",
    host="db",
    database="main_db"
)

engine = create_engine(url)