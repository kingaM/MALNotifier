import requests

def fbNotify(fbId, animeTitle, airDate):
    template = "New anime: " + animeTitle + " - Airing on: " + airDate
    url = "https://graph.facebook.com/" + str(fbId) + "/notifications?access_token=817587931587918|a1393c70ae38ea35ff7b10ba17b73def&template=" + template + "&href="
    r = requests.post(url)
