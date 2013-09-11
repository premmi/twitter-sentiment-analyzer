import sys
import json

def lines(fp):
    return fp.readlines()

def generate_tweet_list(file):
    hashtags_dict = {}
    lines_in_file = lines(file)
    for line in lines_in_file:
        tweet_result = json.loads(line)        
        key = "entities"  
        if key in tweet_result:
            hashtags = tweet_result[key]['hashtags']
            if hashtags:
                for index in range(0, len(hashtags)):
                    hashtag = hashtags[index]['text']
                    if hashtag in hashtags_dict:
                        hashtags_dict[hashtag] += 1
                    else:
                        hashtags_dict[hashtag] = 1
    
    sorted_hashtags = sorted(hashtags_dict, key=hashtags_dict.get, reverse=True)  
    top_hashtags = sorted_hashtags[:10]   
    for tag in top_hashtags:
        print tag, float(hashtags_dict[tag])                  
      

def main():
    tweet_file = open(sys.argv[1])
    generate_tweet_list(tweet_file)

if __name__ == '__main__':
    main()