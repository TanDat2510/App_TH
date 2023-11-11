from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


import App
from App import db


class Category(db.Model):
    __tablename__= 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Products',backref='category',lazy=True)


class Products(db.Model):
    id=Column(Integer,primary_key=True, autoincrement=True)
    name= Column(String(50), nullable=False,unique=True)
    price=Column(Float,default=0)
    image=Column(String(100))
    id_category=Column(Integer,ForeignKey(Category.id),nullable=False)


if __name__=='__main__':
    from App import App
    with App.app_context():
        #c1 = Category(name='Mobile')
        #c2 = Category(name='Tablet')

        #db.session.add(c1)
        #db.session.add(c2)
        #db.session.commit()
        #db.create_all()
        p1= Products(name= 'Iphone 15 Pro max',price=20000000,id_category='1',
                     image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-pro-max_3.png')
        p2 = Products(name='Iphone 13 Pro Max', price=30000000,id_category='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/3/_/3_51_1_2_2_1_1_2.jpg')
        p3 = Products(name='Galaxy S23 Ultra', price=25000000,id_category='2',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/2/s23-ultra-xanh-1.png')
        p4 = Products(name='iPad Pro 2018', price=10000000,id_category='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/ipad-pro-13-select-202210.png')
        p5 = Products(name='Xiaomi Black Shark 4s', price=255000000,id_category='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-black-shark-5.png')
        db.session.add([p1,p2,p3,p4,p5])
        db.session.commit()