import requests
import xml.etree.ElementTree as ET
from db import DBHelper

class AniDB:

    def __init__(self):
        pass
        # Start threads

    def downloadAllShows(self):
        r = requests.get('http://anidb.net/api/anime-titles.xml.gz', stream=True)
        with open('./allshows.txt', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        self.addNewShows()

    def addNewShows(self):
        db = DBHelper()
        lastId = db.retrieveData("SELECT * FROM shows ORDER BY showId DESC LIMIT 1", ())
        if len(lastId) > 0:
            lastId = lastId[0][0]
        else:
            lastId = 0
        tree = ET.parse('./allshows.xml')
        root = tree.getroot()
        for child in root:
            id =  int(child.attrib['aid'])
            if id > lastId:
                db.executeQuery("INSERT INTO shows (showId) VALUES (" + str(id) + ")", ())
                for title in child:
                    lang = title.attrib['{http://www.w3.org/XML/1998/namespace}lang']
                    if (lang == "en") or (lang == "x-jat"):
                        db.executeQuery("INSERT INTO titles (showId, title) VALUES (" + str(id) + ", %s)", (title.text,))


if __name__ == '__main__':
    adb = AniDB()
    adb.addNewShows()
