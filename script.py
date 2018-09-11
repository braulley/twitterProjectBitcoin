import time
import datetime
import tweepy as tweepy
import xlsxwriter
from pymongo import MongoClient
from textblob import TextBlob as tb

client = MongoClient()

# credentials from https://apps.twitter.com/
consumerKey = "IJZz9RAdLAWnaBonIusTEL2l8"
consumerSecret = "e8DxRpcQMKP273T5TqzkVQgqAE9yCQbaHjL7Jc8bZt3Vn7TGBY"
accessToken = "272213908-PPoWkCYIi6hdHrMubmrWRxDMky1be7K9XE7VHdaX"
accessTokenSecret = "LwTJnBipVj3oltNiiVt2IBMjOf9GDkQyy6ZXGvQUjWV33"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

client = MongoClient('mongodb://braulley:tcc1234@ds149672.mlab.com:49672/twitter_search')

db = client.twitter_search
collection = db.twitter


tweets = []

analysis = None


#public_tweets = api.search('bitcoin')

def callTwitter():
    for tweet in tweepy.Cursor(api.search, q='bitcoin', lang='en').items(300):
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            print(tweet.text)
            analysis = tb(tweet.text)
            polarity = analysis.sentiment.polarity
            tweet.polarity = polarity
            tweets.append(tweet)
            print(tweet.created_at)
            print(tweet.text)
            print(tweet.retweet_count)
            print(tweet.polarity)




#for k in range(1,300000):
#   print(k)
#callTwitter()


print('DEZ')
time.sleep(10)

print('---------------------------------------------------------')
print('cinco')
time.sleep(5)

#workbook = xlsxwriter.Workbook('bitcoin' + ".xlsx")
#worksheet = workbook.add_worksheet()
#row = 0
for tweet in tweets:
    post = {"text": '',
            "tweet_created": tweet.created_at,
            "polarity": tweet.polarity,
            "date_create": datetime.datetime.utcnow(),
            "retweet_count": tweet.retweet_count,
            "lang": tweet.lang
            }
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    #worksheet.write_string(row, 0, str(tweet.id))
    #worksheet.write_string(row, 1, str(tweet.created_at))
    #worksheet.write(row, 2, tweet.text)
    #worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    #worksheet.write_string(row, 4, str(tweet.polarity))
    #row += 1

#workbook.close()
print("Excel file ready")