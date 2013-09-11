import sys
import json

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
    lines_in_file = lines(file)
    for line in lines_in_file:
        tweet_result = json.loads(line)
        key = 'text'
        if key in tweet_result:
            tweet_words = tweet_result[key].split()
            tweets.append(tweet_words)              
    return tweets  

def generate_tweet_score(dict, tweets):
    tweet_scores = []
    for tweet in tweets:
        score = 0.0
        for word in tweet:
            if word in dict:
                score += dict[word]
        tweet_scores.append(score)
    return tweet_scores 

def generate_sentiment_score(tweet_scores, dict, tweets):
    terms = {} 
    for tweet in range(0, len(tweets)):
        for word in tweets[tweet]:
            if not(word in dict):
            	if word in terms:
            		terms[word][0] += tweet_scores[tweet]
            		terms[word][1] += 1
            	else:
            	    terms[word]	= [tweet_scores[tweet], 1]
    terms_metric = {}
    for term in terms:
    	terms_metric[term] = terms[term][0] / terms[term][1]
        print term.encode('utf-8') + " " + str(terms_metric[term])

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment_dict = generate_sentiment_dict(sent_file)
    tweets = generate_tweet_list(tweet_file)
    tweet_scores = generate_tweet_score(sentiment_dict, tweets)
    generate_sentiment_score(tweet_scores, sentiment_dict, tweets)   


if __name__ == '__main__':
    main()
