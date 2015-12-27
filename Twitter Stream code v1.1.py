from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = "JSI0zk2vup1QCn3cUOxeaHoyn"
csecret = "B3m0E6TFaaJZ8Tr5zp2d4wkhoCAv0QdFGeDd8DU0T0u8sasHjN"
atoken = "4655901510-PlL0MQ4RN9Wfm1jYrkEqGITmsWe1ucWqJkWtu2y"
asecret = "A75Pn2SL7hd34OcDOLb9X7p8Xgk6HuLYNmyJjOeLna2hn"

class listener(StreamListener):

    def on_data(self,data):
        try:

            tweet = data.split(',"text":"')[1].split('","source')[0]
            print tweet
            saveThis = data 
            #str(time.time()) + '::'+ tweet
            saveFile = open('output_new.txt','a')
            saveFile.write(saveThis)
            #saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed ondata,' ,str(e)
            time.sleep(5)

    def on_error(self,status):
        print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["Putin"],languages=["en"])
