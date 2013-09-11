import sys
import json

def lines(fp):
    return fp.readlines()

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

def generate_terms_dict(tweets):
    terms = {} 
    for tweet in range(0, len(tweets)):
        for word in tweets[tweet]:
            if word in terms:
                terms[word] += 1
            else:
                terms[word]	= 1
    return terms

def compute_frequency(terms):
    total_occurance = sum(terms.itervalues()) 
    for term in terms:
        frequency = float(terms[term]) / total_occurance
        print term.encode('utf-8'), frequency

def main():
    tweet_file = open(sys.argv[1])
    tweets = generate_tweet_list(tweet_file)
    terms_dict = generate_terms_dict(tweets)
    compute_frequency(terms_dict)

if __name__ == '__main__':
    main()