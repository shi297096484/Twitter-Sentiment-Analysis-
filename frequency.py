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
        twitter_list_dict.append(json.loads(line))
    return twitter_list_dict
   
    
def main():

    tweets = tweet_dict(twitterData)
    term_count = {}


    for index in range(len(tweets)):
        tweet_word = tweets[index]["text"].split()
        for word in tweet_word:
            word = word.encode("utf-8")
            word = word.lower()
            word = word.strip('?:!.,;"!@#')
            word = word.replace("\n", "")
            term_count[word] = 0
        
    for index in range(len(tweets)):
        tweet_word = tweets[index]["text"].split()
        for word in tweet_word:
            word = word.encode("utf-8")
            word = word.lower()
            word = word.strip('?:!.,;"!@#')
            word = word.replace("\n", "")
            term_count[word] = term_count[word]+1

    for key in term_count.keys():
        key_freq = float(term_count[key])/len(term_count)
        adjkey_freq = "%.3f"%key_freq
        print key + " "+ adjkey_freq
        

if __name__ == '__main__':
    main()
