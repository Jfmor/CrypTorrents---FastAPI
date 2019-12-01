
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from database.database import Database


app = FastAPI()
db = Database()

app.mount("/static", StaticFiles(directory="../static"), name="static")

#Templates directory instance
templates = Jinja2Templates(directory = "../templates")

@app.get("/")
async def root(request: Request):
    d: dict = {
        "request" : request,
        "torrents" : db.get_none()
    }
    return templates.TemplateResponse("base.html", d)


@app.get("/torrent/{torrent}")
async def display_torrent(request: Request, torrent: str):
    d: dict = {
        "request" : request,
        "torrents" : db.get_torrents(torrent),
    }
    return templates.TemplateResponse("torrent.html", d)