from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean
from sqlalchemy.orm import Session

engine = create_engine('postgresql+psycopg2://postgres:Dont_Do_It@localhost:5432/my1')

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    # author = Column(String)
    # pages = Column(Integer)
    # published = Column(Date)

    # def __repr__(self):
    #     return "<Book(title='{}', author='{}', pages={}, published={})>" \
    #         .format(self.title, self.author, self.pages, self.published)
    def add(self):
        session = Session(engine)
        session.add(self)
        session.commit()
        session.close()

class Message(Base):
    __tablename__ = 'Message'
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    date = Column(DateTime)
    text = Column(String)

    def add(self):
        session = Session(engine)
        session.add(self)
        session.commit()
        session.close()

class FromSomeone(Base):
    __tablename__ = 'FromSomeone'
    id = Column(Integer, primary_key=True)
    someone_id = Column(Integer)
    message_id = Column(Integer)
    is_bot = Column(Boolean)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    language_code = Column(String)

    def add(self):
        session = Session(engine)
        session.add(self)
        session.commit()
        session.close()


class Entities(Base):
    __tablename__ = 'Entities'
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    offset = Column(Integer)
    length = Column(Integer)
    type = Column(String)

    def add(self):
        session = Session(engine)
        session.add(self)
        session.commit()
        session.close()

Base.metadata.create_all(engine)