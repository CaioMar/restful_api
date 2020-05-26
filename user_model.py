from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

engine = create_engine('sqlite:///data.db', echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

session = Session()

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String)

    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname

    def __repr__(self):
        return "<UserModel name:%s>" %self.name

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

Base.metadata.create_all(engine)

caio = UserModel('Caio','Phodao')
juliana = UserModel('Juliana','Moli')

session.add_all([caio, juliana])

session.commit()

print(session.query(UserModel).all())

print(UserModel.find_by_name('Caio'))