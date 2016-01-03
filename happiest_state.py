import sys
import json

sentimentData = sys.argv[1] #AFIN-111.txt
twitterData = sys.argv[2] #output.txt

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
    
def sentiment_dict(sentimentData):
    ''' (file) -> dictionary
    This method should take your sentiment file
    and create a dictionary in the form {word: value}
    '''
    afinnfile = open(sentimentData)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = float(score)  # Convert the score to an integer.

    return scores # Print every (term, score) pair in the dictionary
    
def main():
    tweets = tweet_dict(twitterData)
    sentiment = sentiment_dict(sentimentData)
    state_dict = dict()
    

    '''Create a method below that loops through each tweet in your 
    twees_list.  For each individual tweet it should add up you sentiment 
    score, based on the sent_dict.
    '''
    for index in range(len(tweets)):
        if all(k in tweets[index].keys() for k in ("text","place")):
            if not(tweets[index]["place"] == None):
                if tweets[index]["place"]["country_code"] == "US":
                    if len(tweets[index]["place"]["full_name"].split()[1]) == 2:
                        tweet_state = tweets[index]["place"]["full_name"].split()[1]
                   
                        tweet_word = tweets[index]["text"].split()
                        sent_score = 0
                        for word in tweet_word:
            
                            if word.encode('utf-8') in sentiment.keys():
                                sent_score = sent_score + float(sentiment[word])
                            else:
                                sent_score = sent_score

                        if tweet_state in state_dict.keys():
                            state_dict[tweet_state].append(sent_score)
                        else:
                            state_dict[tweet_state] = []
                            state_dict[tweet_state].append(sent_score)


    state_score = 0
    statescore_dict = {}
    max_score = 0
    happiest_state = ""
    for state in state_dict.keys():
        statescore_dict[state] = 0
        for score in state_dict[state]:
            statescore_dict[state] = statescore_dict[state] + score
        statescore_dict[state] = statescore_dict[state]/len(state_dict[state])
        if happiest_state == "" or statescore_dict[state] > max_score:
            max_score = statescore_dict[state]
            happiest_state = state
    print happiest_state


    
if __name__ == '__main__':
    main()
