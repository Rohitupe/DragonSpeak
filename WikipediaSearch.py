import wikipedia
from SaySpeak import say

def wikiSearch(search):
    """ Search on wikipedia """
    if "wikipedia" in search.lower():
        say("Searching on Wikipedia......")
        search = search.replace("on wikipedia","")
        search = search.replace("search for","")
        result = wikipedia.summary(search,sentences=1)
        print(result)
        say(result)
        print(search)

wikiSearch("search for gravitational force on wikipedia")

