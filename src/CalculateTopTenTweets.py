#!/usr/bin/env python3
import TwitterSearch
from TopTenTweet import TopTenTweet, Base
from Tweet import Tweet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class CalculateTopTenTweets():
    def __init__(self, authors):
        self.connection_string= "postgresql+psycopg2://postgres:postgres@localhost:5432/project_tweets"
        self.authors = authors
        self.calculate_top_tweets()
        self.session = None

    def calculate_top_tweets(self):
        self.session = self.start_db_session()

        top_tweets = self.get_top_tweets()
        print(top_tweets)
        for tweet in top_tweets:
            top_ten = self.convert_top_ten(tweet)
            self.session.add(top_ten)

        self.session.commit()

        self.session.close()
       
    def convert_top_ten(self, tweet):
        return TopTenTweet(
            tweet.id,
            tweet.text,
            tweet.author,
            tweet.created_at,
            tweet.public_metrics,
            tweet.like_count
        )

    def get_top_tweets(self):
        top_tweets = []
        all_tweets = self.session.query(Tweet).all()

        for author in self.authors:
            author_top = [t for t in all_tweets if t.author == author] 
            author_top.sort(key=lambda x: x.like_count, reverse=True)
            top_tweets.extend(author_top[:10])

        return top_tweets

    def start_db_session(self):
        engine = create_engine(self.connection_string, echo=True)
        # create table if it doesn't exist
        Base.metadata.create_all(engine, checkfirst=True)

        Session = sessionmaker(bind=engine)

        return Session()

if __name__ == '__main__':
    authors = ['paulg', 'r00k', 'brennandunn', 'naval', 'dvassallo', 'p']
    CalculateTopTenTweets(['patio11'])
