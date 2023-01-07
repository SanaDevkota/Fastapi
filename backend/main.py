from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from db.session import engine   
from db.base_class import Base
from apis.base import api_router


def include_router(app):
    app.include_router(api_router)


def configure_static(app):  
    # this is going to inform that we are going to keep all our static files in a folder named 'static' and whenever it has to search for static file say an image , don't search here and there. it will be in inside static folder only 
    app.mount("/static", StaticFiles(directory="static"), name="static") 

def create_tables():           
	Base.metadata.create_all(bind=engine)



def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app) 
    create_tables()
    return app
app = start_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1",reload=True,port=8000)

