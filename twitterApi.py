#!/usr/bin/env python3
import credentials
import requests
import pprint 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker




def sql_alchemy_example():
    connection_string = "postgresql+psycopg2://postgres:postgres@localhost:5432/tweets"
    engine = create_engine(connection_string, echo=True)
    Base = declarative_base()

    class User(Base):
        __tablename__ = 'users'
    
        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)
        nickname = Column(String)
    
        def __repr__(self):
           return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)
    Base.metadata.create_all(engine)
    ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(ed_user)
    our_user = session.query(User).filter_by(name='ed').first()
    print(our_user)
    session.add_all([
        User(name='wendy', fullname='Wendy Williams', nickname='windy'),
        User(name='mary', fullname='Mary Contrary', nickname='mary'),
        User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)

    #session.commit()

def sql_alchemy_twitter_example():

    connection_string = "postgresql+psycopg2://postgres:postgres@localhost:5432/tweets"
    engine = create_engine(connection_string, echo=True)
    Base = declarative_base()

    class Tweet(Base):
        __tablename__ = 'tweets'
    
        id = Column(String, primary_key=True)
        text = Column(String)
        author = Column(String)

        def __repr__(self):
           return "<Tweet (text='%s', author='%s')>" % (
                                self.text, self.author)

    Base.metadata.create_all(engine)
    paulg_tweet = Tweet(id='0', text='example paulg tweet', author='paulg')

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(paulg_tweet)
    our_tweet = session.query(Tweet).filter_by(author='paulg').first()
    print(our_tweet)

    #session.add_all([
    #    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    #    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    #    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

    #for instance in session.query(User).order_by(User.id):
    #    print(instance.name, instance.fullname)
 

Base = declarative_base()
class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(String, primary_key=True)
    text = Column(String)
    author = Column(String)

    def __repr__(self):
       return "<Tweet (text='%s', author='%s')>" % (
                            self.text, self.author)

def start_db_session():
    connection_string = "postgresql+psycopg2://postgres:postgres@localhost:5432/tweets"
    engine = create_engine(connection_string, echo=True)

    Session = sessionmaker(bind=engine)

    return Session()

def twitter_search(url):
    headers = {"Authorization": f"Bearer {credentials.bearer_token}"}
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


def main():
    url = "https://api.twitter.com/2/tweets/search/recent?query=from:paulg"
    twitter_search(url)

if __name__ == '__main__':
    main()
