import urllib
import json

for i in range(1, 11):
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=" + str(i))
    result = json.load(response)
    tweets_dict = result['results']

    for tweets in range(0, len(tweets_dict)-1):
        tweet_contents = tweets_dict[tweets]
        unicode_string = tweet_contents['text']
        encoded_string = unicode_string.encode('utf-8')
        print encoded_string