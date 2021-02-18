import tweepy, json

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets Newtownards.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
    #    tweet_list.append(status)   # new line added from Hugo video
        self.num_tweets += 1
        if self.num_tweets < 5:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

access_token = "2929567025-d4d2CZH5WiKw6jr98crUNS98kzEhIWO80OBXkxH"
access_token_secret = "jYYjPtoq2snfPQu2G9nrZYwHwZefezVU1suOAloUrLNOj"
consumer_key = "ddeXGc2iCAWtA01vzGGIG6ojY"
consumer_secret = "YTgj3O9bnpC8APCzDW0erJXFb21X3O1R6oVl4FqLkOHpEbOYua"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize Stream listener
l = MyStreamListener()

# Create your Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
#stream.filter(track=['clinton', 'trump', 'sanders', 'cruz', 'biden', 'covid'])
stream.filter(track=['belfast', 'enniskillen'])