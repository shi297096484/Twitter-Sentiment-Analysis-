from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = "JSI0zk2vup1QCn3cUOxeaHoyn"
csecret = "B3m0E6TFaaJZ8Tr5zp2d4wkhoCAv0QdFGeDd8DU0T0u8sasHjN"
atoken = "4655901510-PlL0MQ4RN9Wfm1jYrkEqGITmsWe1ucWqJkWtu2y"
asecret = "A75Pn2SL7hd34OcDOLb9X7p8Xgk6HuLYNmyJjOeLna2hn"

class listener(StreamListener):

    def on_data(self,data):
        print data
        return True

    def on_error(self,status):
        print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["Putin"],languages=["en"])
