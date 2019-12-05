import sys

from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette import responses
sys.path.append("./modules/database")
from database import Database
app = FastAPI()
db = Database()

app.mount("/static", StaticFiles(directory="static"), name="static")

#Templates directory instance
templates = Jinja2Templates(directory = "./templates")


@app.get("/")
async def root(request: Request):
    '''
    Main page, base root endpoint.

    @returns {HTML template} main page template.
    '''
    d: dict = {
        "request" : request,
        "torrents" : db.get_none()
    }
    return templates.TemplateResponse("base.html", d)


@app.get("/torrents/{torrent}")
async def display_torrent_page(request: Request, torrent: str):
    '''
    Retrieves a torrent based on the torrent query, with top 3 results.

    @returns {HTML Template} top 3 torrent table page based on query.
    '''
    d: dict = {
        "request" : request,
        "torrents" : db.get_torrents(torrent),
    }
    return templates.TemplateResponse("torrent.html", d)