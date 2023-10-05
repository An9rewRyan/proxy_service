from celeryconfig import app
from webshare import Updator
from database import engine
from models import Proxy
import logging
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

@app.task
def update():
    updator = Updator()
    proxies = updator.load_proxies()
    with Session(engine) as session:
        num_rows_deleted = session.query(Proxy).delete()
        for proxy in proxies:
            proxy = Proxy(**proxy)
            session.add(proxy)
        session.commit()
    logger.info(f"Deleted {num_rows_deleted} rows")
