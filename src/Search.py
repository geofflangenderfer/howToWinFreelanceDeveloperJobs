#!/usr/bin/env python3
import Tweet
import credentials
import requests
import pprint 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Search():
    headers = {"Authorization": f"Bearer {credentials.bearer_token}"}
    response_json
    def twitter_search(url):
        response_json = requests.get(url, headers=headers).json()
        
        session = start_db_session()
    
        tweet_objects = response_json["data"]
        for obj in tweet_objects:
            tweet = Tweet(
                id=obj["id"],
                text=obj["text"],
                author='paulg'
            )
            session.add(tweet)
    
        session.commit()
        session.close()
    
        for instance in session.query(Tweet).order_by(Tweet.id):
            print(instance.id, instance.text)



def start_db_session():
    connection_string = "postgresql+psycopg2://postgres:postgres@localhost:5432/tweets"
    engine = create_engine(connection_string, echo=True)

    Session = sessionmaker(bind=engine)

    return Session()


def main():
    url = "https://api.twitter.com/2/tweets/search/recent?query=from:paulg"
    twitter_search(url)

if __name__ == '__main__':
    main()
