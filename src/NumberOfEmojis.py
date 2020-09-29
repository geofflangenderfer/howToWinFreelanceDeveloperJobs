from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class NumberOfEmojis(Base):
    __tablename__ = 'numberofemojis'

    id = Column(String, primary_key=True)
    number_emojis = Column(Integer)

    def __init__(self, id_string, number_emojis):
        self.id = id_string
        self.number_emojis= number_emojis

    def __repr__(self):
       return "<NumberOfEmojis (id='%s', number_emojis='%s')>" \
               % (self.id, self.number_emojis)
