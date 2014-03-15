import requests
import xml.etree.ElementTree as ET
from db import DBHelper

class MAL:

    # TODO: Fix the api
    def getXML(self, malusername):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; AskTB5.6)',        
            }
        payload = {'u': malusername, 'status': 'all', 'type' : 'anime'}
        r = requests.get("http://myanimelist.net/malappinfo.php", params=payload, headers=headers)
        print r.url
        print r.content
        print r.text

    def parseXML(self, username):
        tree = ET.parse(username + '.xml')
        root = tree.getroot()
        for anime in root.findall('anime'):
            try:
                print anime.find('series_title').text
                print anime.find('my_score').text
            except Exception, e:
                pass

    def getUsers(self):
        db= DBHelper()
        for user in  db.retrieveData("SELECT * FROM `users`"):
            self.parseXML(user[3])

mal = MAL()
mal.getUsers()