from tpb import TPB
from tpb import ORDERS
from typing import List

class Database():
    
    def __init__(self):

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

        for torrent in self.website.search(req).order(ORDERS.SEEDERS.DES):
            if counter <= 2:
                obj.append(
                    {
                        "name" : torrent.title,
                        "magnet" : torrent.magnet_link,
                        "image" : "123",
                    }
                )
            counter += 1
        return obj