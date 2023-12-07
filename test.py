from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Float, Column
import sqlalchemy
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class MyGoods(Base):
    __tablename__ = "my_goods"
    id = Column(Integer, primary_key=True)
    Good_name = Column(String(50))
    Price = Column(Float)
    Amount = Column(Integer)

    def __init__(self,good_name,good_price,good_amount):
        self.Good_name = good_name
        self.Price = good_price
        self.Amount = good_amount




engine = sqlalchemy.create_engine('sqlite:///D:/Proj/pythonProject/blogsite/db.sqlite3')
session = sessionmaker(bind=engine)
connection = session()
new_good = MyGoods("jake",5,125)
connection.add(new_good)
connection.commit()