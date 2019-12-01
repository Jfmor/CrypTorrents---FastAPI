from requests import Session
import json

class ImageAPI():

    def __init__(self):
        self.s = Session()

    def get_image(self, name: str) -> str:
        
        '''
        Gets an image URL from SerpAPI

        @param {str} name: name of the image to lookup
        @return {str} url of the thing to look up (movie, game, book, etc)
        '''

        headers: dict = {
            "Accept" : "application/json",
        }
        r = self.s.get(
            url = f'http://api.duckduckgo.com/?format=json&pretty=1&q={name}',
            verify = False,
            headers = headers
        )

        d: dict = json.loads(json.dumps(r.json()))
        return str(d["Image"])