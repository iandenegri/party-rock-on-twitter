import twitter

import twitter_config  # Local file used to store private data like keys, etc.

api = twitter.Api(consumer_key=twitter_config.consumer_key, 
consumer_secret=twitter_config.consumer_secret, 
access_token_key=twitter_config.access_token_key, 
access_token_secret=twitter_config.access_token_secret)

tweet_id_to_spam = 1238816397658030080

if api.GetStatus(tweet_id_to_spam).current_user_retweet:
    current_party_rockers_rt = api.GetStatus(tweet_id_to_spam).current_user_retweet
    api.DestroyStatus(current_party_rockers_rt)
api.PostRetweet(tweet_id_to_spam)
