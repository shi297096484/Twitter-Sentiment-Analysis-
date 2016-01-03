import sys
import json

twitterData = sys.argv[1] #output.txt

def tweet_dict(twitterData):  
    ''' (file) -> list of dictionaries
    This method should take your output.txt
    file and create a list of dictionaries.
    '''
    twitter_list_dict = []
    twitterfile = open(twitterData)
    for line in twitterfile:
        #twitter_list_dict.append(json.loads(line.decode('utf-8-sig')))
        twitter_list_dict.append(json.loads(line))
    return twitter_list_dict
    #return data_read["text"]
    
    
def main():
    tweets = tweet_dict(twitterData)
    tweet_hashtags = []

    for index in range(len(tweets)):
        if all(k in tweets[index].keys() for k in ("text","entities")):

            if not(tweets[index]["entities"] == None):
                if not (tweets[index]["entities"]["hashtags"] == []):
                    for indx in range(len(tweets[index]["entities"]["hashtags"])):
                    
                        hashtags = tweets[index]["entities"]["hashtags"][indx]["text"]
                        tweet_hashtags.append(hashtags.encode('utf-8').lower())

    hashtags_dict = {}

    for hashtag in tweet_hashtags:
        hashtags_dict[hashtag] = 0

    for hashtag in tweet_hashtags:
        hashtags_dict[hashtag] = hashtags_dict[hashtag] + 1

    for name, freq in sorted(hashtags_dict.iteritems(), key=lambda (k, v): (-v, k))[:10]:
        print name, freq

    

    
if __name__ == '__main__':
    main()
