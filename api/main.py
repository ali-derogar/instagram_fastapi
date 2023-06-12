from fastapi import FastAPI
from db.models import base
from db.databases import engine
from fastapi.staticfiles import StaticFiles
from router import user , post , authentication , comments



base.metadata.create_all(engine)
app = FastAPI()
app.mount("/uploaded_file",StaticFiles(directory="uploaded_file") , name='files')
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comments.router)

@app.get('/')
def start():
    return "hello to here"