from sqlalchemy import Column, Integer, String, Float, ForeignKey,Enum
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import  UserMixin
import enum

import App
from App import db


class UseRoleEnum(enum.Enum):
    USER=1
    ADMIN=2

class User(db.Model):
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50),nullable=False)
    username=Column(String(50),nullable=False,unique=True)
    password=Column(String(100),nullable=False)
    avatar=Column(String(300),default='https://png.pngtree.com/png-clipart/20190920/original/pngtree-user-flat-character-avatar-png-png-image_4643588.jpg')

    user_role=Column(Enum(UseRoleEnum),default=UseRoleEnum.USER)


    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__= 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Products',backref='category',lazy=True)

    def __str__(self):
        return self.name


class Products(db.Model):
    id=Column(Integer,primary_key=True, autoincrement=True)
    name= Column(String(50), nullable=False,unique=True)
    price=Column(Float,default=0)
    image=Column(String(300))
    id_category=Column(Integer,ForeignKey(Category.id),nullable=False)


    def __str__(self):
        return self.name


if __name__=='__main__':
    from App import App
    with App.app_context():
        db.create_all()

        import hashlib
        u=User(name='Admin',
               username='admin',
               password=str(hashlib.md5('abc123'.encode('utf-8')).hexdigest()),
               user_role=UseRoleEnum.ADMIN)
        # db.session.add(u)
        # db.session.commit()
        # db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Products(name='Iphone 15 Pro max', price=20000,id_category='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-pro-max_3.png')
        p2 = Products(name='Iphone 13 Pro Max', price=30000, id_category='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/3/_/3_51_1_2_2_1_1_2.jpg')
        p3 = Products(name='Galaxy S23 Ultra', price=25000, id_category='2',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/2/s23-ultra-xanh-1.png')
        p4 = Products(name='iPad Pro 2018', price=100000, id_category='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/ipad-pro-13-select-202210.png')
        p5 = Products(name='Xiaomi Black Shark 4s', price=255000, id_category='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-black-shark-5.png')

        db.session.add_all([p1,p2,p3,p4,p5])
        db.session.commit()

