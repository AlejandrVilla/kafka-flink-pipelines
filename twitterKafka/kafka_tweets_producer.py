# import tweepy

from json import dumps, loads
from kafka import KafkaProducer
from rich import print
from time import sleep

producer = KafkaProducer(
    bootstrap_servers=[
        'ip-172-31-85-30.ec2.internal:9092'
    ],
    value_serializer=lambda K:dumps(K).encode('utf-8')
)


# to read keys from secret txt file
# with open('/path/to/secrets.txt') as f:
#     for line in f:
#         if '=' in line:
#             key, value = line.strip().split(' = ')
#             if key == 'CONSUMER_KEY':
#                 CONSUMER_KEY = value.strip("'")
#             elif key == 'CONSUMER_SECRET':
#                 CONSUMER_SECRET = value.strip("'")
#             elif key == 'ACCESS_TOKEN':
#                 ACCESS_TOKEN = value.strip("'")
#             elif key == 'ACCESS_TOKEN_SECRET':
#                 ACCESS_TOKEN_SECRET = value.strip("'")


# auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

# api=tweepy.API(auth)
# cursor=tweepy.Cursor(api.search_tweets,q='music', lang="en",tweet_mode='extended').items(100)

json_file_path = '../data.json'

with open(json_file_path, 'r') as file:
    for line in file:
        tweet_data = loads(line)
        
        id_str = tweet_data['id_str']
        username = tweet_data['username']
        tweet = tweet_data['tweet']
        location = tweet_data['location']
        created_at = tweet_data['created_at']
        retweet_count = tweet_data['retweet_count']
        favorite_count = tweet_data['favorite_count']
        followers_count = tweet_data['followers_count']
        lang = tweet_data['lang']
        coordinates = tweet_data['coordinates']
        
        cur_data={
            "id_str": id_str,
            "username": username,
            "tweet": tweet,
            "location": location,
            "retweet_count": retweet_count,
            "favorite_count": favorite_count,
            "followers_count": followers_count,
            "lang": lang
        }
        # "coordinates": tweet.coordinates
        producer.send('my-topic-test', value=cur_data)
        print(cur_data)
        sleep(0.5)
