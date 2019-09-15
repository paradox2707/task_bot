from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
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


Base.metadata.create_all(engine)