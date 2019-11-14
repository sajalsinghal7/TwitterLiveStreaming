from django.shortcuts import render
from django.http import HttpResponse
import tweepy
#Consumer API keys
API_key = "oDvyHQl4wWO84Jcm6SelK58no"
API_secret_key = "vKRMxB5kGhd85Esh0hNkvFLnNPFJRfCCzW5R35v58Q21UjliNK"

#Access token & access token secret
Access_token = "4049924489-A41wgzQnc4Zt2UBnGTMO0E2A2YkgDwwsYbl5fkV"
Access_token_secret = "L0TiAWUMf7VXDmecdFRZohnFd2E6z40Wd6Ec1hGD1dEzG"

#Live Data
liveData = "Hi Sajal"


#Step 1: Creating a StreamListener
class TwitterStreamListner(tweepy.StreamListener):
    def on_status(self, status):
        self.addNewTweetToDisplay(status)
        return True
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
    def addNewTweetToDisplay(self, data):
        print(data)
        liveData = data

#Step 2: Creating a Stream
class TwitterStream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)
    def start(self, listOfKeyord):
        self.stream.filter(track=listOfKeyord)

#Step 3: Starting a Stream
def index(request):
    listener = TwitterStreamListner()
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(Access_token, Access_token_secret)
    stream = TwitterStream(auth, listener)
    stream.start(['Pradesh'])
    return HttpResponse(liveData)

