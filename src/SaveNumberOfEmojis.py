#!/usr/bin/env python3
from NumberOfEmojis import NumberOfEmojis, Base
from CalculateEmojis import CalculateEmojis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SaveNumberOfEmojis():
    def __init__(self, number_of_emojis):
        self.connection_string= "postgresql+psycopg2://postgres:postgres@localhost:5432/tweets"
        self.number_of_emojis = number_of_emojis
        self.save_number_of_emojis()

    def save_number_of_emojis(self):
        session = self.start_db_session()

        for emoji in self.number_of_emojis:
            session.add(emoji)

        session.commit()
        for emoji in self.number_of_emojis:
            print(emoji)
        

        session.close()

    def start_db_session(self):
        engine = create_engine(self.connection_string, echo=True)

        Base.metadata.create_all(engine, checkfirst=True)

        Session = sessionmaker(bind=engine)

        return Session()

if __name__ == '__main__':
    emojis = CalculateEmojis()
    SaveNumberOfEmojis(emojis.number_of_emojis)
    #for tweet in search.tweets:
    #    print(tweet)
