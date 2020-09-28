from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(String, primary_key=True)
    text = Column(String)
    author = Column(String)

    def __init__(self, id_string, text_string, author_string):
        self.id = id_string
        self.text = text_string
        self.author = author_string

    def __repr__(self):
       return "<Tweet (id='%s', text='%s', author='%s')>" % (self.id, self.text, self.author)
