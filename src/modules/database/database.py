import sys
sys.path.append(".")

from tpb import TPB
from tpb import ORDERS
from typing import List
from image_api import ImageAPI

class Database():
    
    def __init__(self):

        self.iAPI = ImageAPI()
        self.website = TPB("https://thepiratebay.org/") #Base URL for ThePirateBay

    def get_none(self) -> List[dict]:
        return [{
            "name" : "",
            "magnet" : "",
            "image" : ""
        }]

    def get_torrents(self, req: str) -> List[dict]:
        counter: int = 0
        obj: List[dict]= []

        button_id: str = "pirate_button_"
        button_count: int = 1

        for torrent in self.website.search(req).order(ORDERS.SEEDERS.DES):
            if counter <= 2:
                obj.append(
                    {
                        "name" : torrent.title,
                        "magnet" : torrent.magnet_link,
                        "image_url" : self.iAPI.get_image(req),
                        "button_id" : button_id + str(button_count),
                    }
                )
            counter += 1
            button_count += 1
        return obj