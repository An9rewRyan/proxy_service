from fastapi import FastAPI
from sqlalchemy.orm import Session
from models import Proxy
app = FastAPI()
from database import engine
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


@app.get("/get_proxies")
def get_proxies():
    proxies = []
    with Session(engine) as session:
        for class_instance in session.query(Proxy).all():
            proxy = vars(class_instance)
            del proxy['_sa_instance_state']
            proxies.append(proxy)
    proxies_json = jsonable_encoder(proxies)
    return JSONResponse(content=proxies_json)


