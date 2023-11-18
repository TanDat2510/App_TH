from App.models import Category, Products, User

def get_categorites():
    return Category.query.all()

def load_products(kw= None):
    prd=Products.query
    if kw:
        prd=prd.filter(Products.name.contains(kw))
    return prd.all()

def get_user_by_id(id):
    return User.query.get(id)