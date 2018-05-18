import tweepy
import textblob
import matplotlib
import matplotlib.pyplot as plt
import numpy
import numpy as np
from textblob import TextBlob

consumer_key = raw_input('Enter your consumer key :')
consumer_secret = raw_input('Enter your consumer secret :')

access_token = raw_input('Enter your access token :')
access_token_secret = raw_input('Enter your access token secret :')
topic = raw_input('Enter the topic on which you want to perform sentiment analysis : ')
def senti_topic(topic):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    public_tweets = api.search(str(topic), count = 200)
    pos = 0
    neg = 0
    neut = 0
    for tweet in public_tweets:
        sc = TextBlob(tweet.text)
        if(sc.sentiment.polarity>0):
            pos=pos+1
        elif (sc.sentiment.polarity<0):
            neg=neg+1
        else:
            neut=neut+1
    return pos,neg,neut,len(public_tweets)

l = senti_topic(topic)

x = ('Positive','Negative','Neutral')
y_pos = np.arange(len(x))
t = [(l[0]*100)/l[3],(l[1]*100)/l[3],(l[2]*100)/l[3]]
plt.bar(y_pos, t, align='center', alpha=0.5,width=.2,color = 'green')
plt.xticks(y_pos, x)
plt.show()


