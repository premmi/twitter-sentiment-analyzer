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

def generate_sentiment_score(dict, tweets):
    for tweet in tweets:
        score = 0.0
        for word in tweet:
            if word in dict:
                score += dict[word]
        print score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment_dict = generate_sentiment_dict(sent_file)
    tweets = generate_tweet_list(tweet_file)
    generate_sentiment_score(sentiment_dict, tweets)     

if __name__ == '__main__':
    main()
