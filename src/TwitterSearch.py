#!/usr/bin/env python3
import Tweet
import auth.credentials
import requests

class TwitterSearch():

    def __init__(self):
        self.headers = {"Authorization": f"Bearer {auth.credentials.bearer_token}"}
        self.url = "https://api.twitter.com/2/tweets/search/recent?query=from:ev"
        self.tweets = self.get_tweets()

    def get_tweets(self):
    
        response_json = self.get_twitter_response_json()
        tweet_objects = response_json["data"]
        tweets = []
        for obj in tweet_objects:
            tweets.append(Tweet.Tweet(
                obj["id"],
                obj["text"],
                'hypefury'
            ))

        return tweets

    def get_twitter_response_json(self):
        response = requests.get(self.url, headers=self.headers)


        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        return response.json()
    

if __name__ == '__main__':
    test = TwitterSearch()
    for tweet in test.tweets:
        print(tweet)
