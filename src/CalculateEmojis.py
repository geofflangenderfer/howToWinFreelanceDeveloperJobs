#!/usr/bin/env python3
import re
from Tweet import Tweet
from NumberOfEmojis import NumberOfEmojis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CalculateEmojis():
    def __init__(self):
        self.connection_string= "postgresql+psycopg2://postgres:postgres@localhost:5432/tweets"
        self.tweets = self.get_tweets()
        self.number_of_emojis = self.create_number_of_emojis()

    def get_tweets(self):
        session = self.start_db_session()

        tweets = []
        for tweet in session.query(Tweet):
            tweets.append(tweet)

        return tweets

        session.close()
    def start_db_session(self):
        engine = create_engine(self.connection_string, echo=True)

        #Base.metadata.create_all(engine, checkfirst=True)

        Session = sessionmaker(bind=engine)

        return Session()
    def get_number_of_emojis(self, text):
        return len(text) - len(self.remove_emojis(text))
    
    def remove_emojis(self, sample):
        emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   "]+", flags=re.UNICODE)

        return emoji_pattern.sub(r'', sample)

    def create_number_of_emojis(self):
        number_of_emojis = []
        for tweet in self.tweets:
            number_of_emojis.append(NumberOfEmojis(
                tweet.id,
                self.get_number_of_emojis(tweet.text)
            ))

        return number_of_emojis



if __name__ == '__main__':
    test = CalculateEmojis()
    #for emoji in test.number_of_emojis:
    #    print(emoji)
