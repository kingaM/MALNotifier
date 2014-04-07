import requests
import threading
import os.path
import xml.etree.ElementTree as ET
from db import DBHelper
from time import sleep
from time import time
import random

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
                # Be nice with the APIs for now ... don't scrape old stuff on the first run
                # self.checkSequel(id)

    def checkSequel(self, id):
        self.getXML(id)
        if not os.path.isfile("./xml/" + str(id) + ".xml"):
            return
        tree = ET.parse("./xml/" + str(id) + ".xml")
        root = tree.getroot()
        if root.find("relatedanime") is None:
            return
        for anime in root.find("relatedanime"):
            if anime.attrib['type'] == "Prequel":
                prequelId = anime.attrib['id']
                db = DBHelper()
                db.executeQuery("UPDATE shows SET sequel=" + str(id) + " WHERE showId=%s", (prequelId,))
                print "Added sequel: " + str(id)

    def getXML(self, id):
        db = DBHelper()
        lastXmlUpdate = db.retrieveData("SELECT lastXmlUpdate FROM shows WHERE showId=%s", (id,))
        if len(lastXmlUpdate) < 1:
            return
        lastXmlUpdate = lastXmlUpdate[0][0]
        if lastXmlUpdate is None or time() - lastXmlUpdate > 604800000: # 1 week
            sleep(2)
            url = "http://api.anidb.net:9001/httpapi?request=anime&client=seqwatcher&clientver=0&protover=1&aid=" + str(id)
            r = requests.get(url)
            xml = r.text.encode('utf-8')
            if "anime id" not in xml: # check the response is valid
                return
            db.executeQuery("UPDATE shows SET xml=%s, lastXmlUpdate=%s WHERE showId=%s", (xml, time(), id))
            print "Updated XML for showId: " + str(id)

    def fillBacklog(self):
        idList = list(range(1,10600))
        while len(idList) > 0:
            sleep(random.randint(5,90))
            id = random.choice(idList)
            self.getXML(id)
            idList.remove(id)


if __name__ == '__main__':
    adb = AniDB()
    # adb.addNewShows()
    adb.fillBacklog()
