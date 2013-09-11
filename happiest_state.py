import sys
import json
import operator

def lines(fp):
    return fp.readlines()

def generate_sentiment_dict(file):
    scores = {}  
    lines_in_file = lines(file) # Initialize an empty dictionary
    for line in lines_in_file:
        term, score = line.split("\t") 
        scores[term] = int(score)
    return scores 

def generate_tweet_list(file):
    tweets = []
    terms_dict = {}
    lines_in_file = lines(file)
    for line in lines_in_file:
        tweet_result = json.loads(line)
        if ('place' in tweet_result) and (tweet_result['place'] is not None):
            if 'country_code' in tweet_result['place'] and tweet_result['place']['country_code'] == 'US':
                if 'full_name' in tweet_result['place'] and tweet_result['place']['full_name'] is not None:
                    state_list = tweet_result['place']['full_name'].split()
                    if len(state_list) == 2 and state_list[1] is not None:
                        state = state_list[1]        
                        if 'text' in tweet_result and tweet_result['text'] is not None:
                        	tweet_words = tweet_result['text'].split()
                        	if state in terms_dict:
                        		for word in tweet_words:
                        			terms_dict[state].append(word)
                        	else:
                        	    terms_dict[state] = tweet_words	
    return terms_dict

def generate_sentiment_score(sentiment_dict, tweets_dict):
    statewise_score_dict = {}
    for state in tweets_dict:
        score = 0.0
        for word in tweets_dict[state]:
            if word in sentiment_dict:
                score += sentiment_dict[word]
        statewise_score_dict[state] = score       
    return statewise_score_dict   

def compute_happiest_state(score_dict):
    print max(score_dict.iteritems(), key=operator.itemgetter(1))[0].encode('utf-8')   

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment_dict = generate_sentiment_dict(sent_file)
    tweets_by_state = generate_tweet_list(tweet_file)    
    statewise_score = generate_sentiment_score(sentiment_dict, tweets_by_state)
    compute_happiest_state(statewise_score)    

if __name__ == '__main__':
    main()