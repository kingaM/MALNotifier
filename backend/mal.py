import requests
import xml.etree.ElementTree as ET
from db import DBHelper
import myemail as email
import os
import json
import sys
import notify
import platform

class MAL:

    # TODO: Fix the api
    def getXML(self, malusername):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; AskTB5.6)',        
            }
        payload = {'u': malusername, 'status': 'all', 'type' : 'anime'}
        r = requests.get("http://myanimelist.net/malappinfo.php", params=payload, headers=headers)
        # print r.url
        # print r.content
        # print r.text

    def parseXML(self, username, fbId=None, titles=[]):
        if platform.system() == "Windows":
            filepath = os.path.dirname(os.path.realpath('../backend/')) + '\\backend\\' + username + '.xml'
        else:
            filepath = os.path.dirname(os.path.realpath('../backend/')) + '/backend/' + username + '.xml'
        try:
            tree = ET.parse(filepath)
        except IOError, e:
            return None
        # tree = ET.parse('../backend/username' + '.xml')
        root = tree.getroot()
        listOfShows = {}
        for anime in root.findall('anime'):
            for title in titles:
                if anime.find('series_title').text in title[0]:
                    tuple = self.parseAniDB(title[1])
                    email.sendMail('kinga.mrugala@gmail.com', tuple[0], tuple[1], tuple[2], "xyz")
                    # print tuple
                    # email.sendMail('kinga.mrugala@gmail.com', tuple[0], tuple[1], tuple[2], "xyz")
                    if fbId is not None:
                        notify.fbNotify(fbId, tuple[1], tuple[0])
                    listOfShows[tuple[1]] = tuple
        for anime in root.findall('anime'):
            if anime.find('series_title').text in listOfShows.keys():
                del listOfShows[anime.find('series_title').text]
        for show in listOfShows.keys():
            pass
            # email.sendMail()
        return listOfShows
                    

    def parseAniDB(self, showId):
        if platform.system() == "Windows":
            filepath = os.path.dirname(os.path.realpath('../backend/')) + '\\backend\\xml\\' + str(showId) + '.xml'
        else:
            filepath = os.path.dirname(os.path.realpath('../backend/')) + '/backend/xml/' + str(showId) + '.xml'
        tree = ET.parse(filepath)
        root = tree.getroot()
        if root.find('startdate') is not None:
            startdate = root.find('startdate').text
        else:
            startdate = "unknown"
        if root.find('description') is not None:
            desc = root.find('description').text
        else:
            desc = "Not available"
        if root.find('titles/title') is not None:
            title = root.find('titles/title').text
        else:
            title = "Not available"

        return (startdate, title, desc, showId)

    def getUsers(self, titles):
        db = DBHelper()
        data = []
        for user in db.retrieveData("SELECT * FROM `users`"):
            data.append(self.parseXML(user[3], int(user[2]), titles))

    def notifyUsers(self, newAnime = [], user=None):
        allTitles = []
        db = DBHelper()
        if not newAnime:
            return 
        for anime in newAnime:
            titles = db.retrieveData("SELECT title FROM titles, shows WHERE titles.showId = shows.showId AND sequel = " + str(anime))
            tmp = []
            for title in titles:
                tmp.append(title[0])
            allTitles.append((tmp, anime,))
        # print allTitles
        # Once no mock data
        # self.getUsers(allTitles)
        if user is not None:
            return self.parseXML(user, fbId=718666456, titles=allTitles)
        else:
            return self.getUsers(allTitles)
        # return self.parseXML("chii", fbId=718666456, titles=allTitles)

mal = MAL()
if len(sys.argv) == 2:
    print json.dumps(mal.notifyUsers([10046, 10048, 10065, 10376, 10517, 10518, 10519, 9284, 9603, 9797, 9807, 9849], sys.argv[1]))
else:
    print json.dumps(mal.notifyUsers([10046, 10048, 10065, 10376, 10517, 10518, 10519, 9284, 9603, 9797, 9807, 9849]))
# mal.parseAniDB(9284)
