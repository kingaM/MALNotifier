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
        r = requests.post("http://myanimelist.net/malappinfo.php?u=" + malusername + "&status=all&type=anime")
        xml = r.text.encode('utf-8')
        return xml

    def parseXML(self, username, useremail, fbId=None, score=0, titles=[], first=False):
        
        root = ET.fromstring(self.getXML(username))
        listOfShows = {}
        for anime in root.findall('anime'):
            for title in titles:
                if (anime.find('series_title').text in title[0]) and (int(anime.find('my_score').text) >= int(score)):
                    tuple = self.parseAniDB(title[1])                    
                    listOfShows[tuple[1]] = tuple
        for anime in root.findall('anime'):
            if anime.find('series_title').text in listOfShows.keys():
                del listOfShows[anime.find('series_title').text]
        if not first:
            for show in listOfShows.keys():
                email.sendMail(useremail, tuple[1], tuple[0], tuple[2], tuple[3])
                if fbId is not None:
                    notify.fbNotify(int(fbId), tuple[1], tuple[0])
        return listOfShows

    #TODO: Move this info to the DB rather than parse it each time
    def parseAniDB(self, showId):
        db = DBHelper()
        xml = db.retrieveData("SELECT xml FROM shows WHERE showId=%s", (showId,))[0][0]
        root = ET.fromstring(xml)
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
            print user[4]
            userdata = self.parseXML(user[3], user[1], user[2], user[4], titles)
            if userdata is not None:
                data.append(userdata)
        return data

    def notifyUsers(self, newAnime = [], user=None):
        allTitles = []
        db = DBHelper()
        if not newAnime:
            return None
        for anime in newAnime:
            titles = db.retrieveData("SELECT title FROM titles, shows WHERE titles.showId = shows.showId AND sequel = " + str(anime))
            tmp = []
            for title in titles:
                tmp.append(title[0])
            allTitles.append((tmp, anime,))
        if user is not None:
            user = db.retrieveData("SELECT * FROM `users` WHERE mal = \"" + user + "\"")
            if len(user) != 1:
                return None
            user = user[0]
            return self.parseXML(user[3], user[1], user[2], 0, titles=allTitles, first=True)
        else:
            return self.getUsers(allTitles)

    def showAllForUser(self, MALname):
        db = DBHelper()
        root = ET.fromstring(self.getXML(MALname))
        listOfShows = {}

        for anime in root.findall('anime'):
            title = anime.find('series_title').text.encode('utf-8')
            sql = "SELECT shows.showId, shows.sequel FROM titles, shows WHERE titles.showId = shows.showId AND title = %s AND sequel IS NOT NULL"
            sequel = db.retrieveData(sql, (title,))
            if len(sequel) > 0:
                tuple = self.parseAniDB(int(sequel[0][1]))                    
                listOfShows[tuple[1]] = tuple

        for anime in root.findall('anime'):
            if anime.find('series_title').text in listOfShows.keys():
                del listOfShows[anime.find('series_title').text]

        return listOfShows

mal = MAL()
if len(sys.argv) == 2:
    MALname = sys.argv[1]
    print json.dumps(mal.showAllForUser(MALname))
else:
    pass
    # print json.dumps(mal.notifyUsers([10376]))
# mal.parseAniDB(9284)
