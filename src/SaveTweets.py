#!/usr/bin/env python3
import TwitterSearch
from Tweet import Tweet 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SaveTweets():
    def __init__(self, tweets):
        self.connection_string= "postgresql+psycopg2://postgres:postgres@localhost:5432/tweets"
        self.tweets = tweets
        self.save_tweets()

    def save_tweets(self):
        session = self.start_db_session()

        for tweet in self.tweets:
            session.add(tweet)

        session.commit()

        session.close()

    def start_db_session(self):
        engine = create_engine(self.connection_string, echo=True)
        Session = sessionmaker(bind=engine)

        return Session()

if __name__ == '__main__':
    search = TwitterSearch.TwitterSearch()
    test = SaveTweets(search.tweets)
    for tweet in search.tweets:
        print(tweet)
