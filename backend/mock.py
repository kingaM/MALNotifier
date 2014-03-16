import anidb

import requests
import threading
import os.path
import xml.etree.ElementTree as ET
from db import DBHelper
from time import sleep

def mockCheckSequel(id):
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

for x in range(1,11000):
    mockCheckSequel(x)
