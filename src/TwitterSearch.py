#!/usr/bin/env python3
import Tweet
import auth.credentials
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TwitterSearch():

    def __init__(self, query_string):
        self.url = "https://api.twitter.com/2/tweets/search/recent"
        self.db_conn_string = "postgresql+psycopg2://postgres:postgres@localhost:5432/tweets"
        self.headers = {"Authorization": f"Bearer {auth.credentials.bearer_token}"}
        self.query_string = query_string
        self.params = self.get_request_params()
        self.response_json = self.get_response_json()
        self.db_engine = create_engine(self.db_conn_string)
        self.db_session = self.get_db_session()
        self.tweets = self.get_tweets()

    def get_response_json(self):
        return requests.get(self.url, params=self.params, headers=self.headers).json()

    def get_request_params(self):
        return {
            "query":self.query_string,
            "max_results":"100"
        }

    def close_session():
        self.db_session.close()
    def get_db_session(self):
        Session = sessionmaker(bind=self.db_engine)

        return Session()

    def get_tweets(self):
    
        tweet_objects = self.response_json["data"]
        tweets = []
        for obj in tweet_objects:
            tweets.append(Tweet.Tweet(
                id=obj["id"],
                text=obj["text"],
                # TODO: decide whether to alter Tweet class
                author='hypefury'
            ))

        return tweets
    

    def save_tweets(self):
        self.db_session.add_all(self.tweets)
        self.db_session.commit()

    def tweets_are_saved(self):
        return len(self.tweets) == len(self.response_json["data"])
    

    def __repr__(self):

        all_repr = ""
        for tweet in self.tweets:
            all_repr += f"{tweet}\n"
        return all_repr



if __name__ == '__main__':
    query = "from:hypefury"
    test = TwitterSearch(query)
    test.save_tweets()
    print(test.tweets)
    print(f"tweets_are_saved {test.tweets_are_saved()}")
    test.db_session.close()
