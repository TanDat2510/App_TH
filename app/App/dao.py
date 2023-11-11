from App.models import Category,Products


def get_categorites():

    return[{
        'id': 1,
        'name': 'Moble'
    },{
        'id': 2,
        'name': 'Table'
    }]

def load_products(kw= None):
    prd= [{
        'id': 1,
        'name': 'Iphone 15 Pro Max',
        'price': 20000000,
        'image':'https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-pro-max_3.png'
    },{
        'id': 2,
        'name': 'Iphone 13 Pro Max',
        'price': 30000000,
        'image':'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/3/_/3_51_1_2_2_1_1_2.jpg'
    },{
        'id': 3,
        'name': 'Galaxy S23 Ultra',
        'price': 25000000,
        'image':'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/2/s23-ultra-xanh-1.png'
    },{
        'id': 4,
        'name': 'iPad Pro 2018',
        'price': 10000000,
        'image':'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/ipad-pro-13-select-202210.png'
    },{
        'id': 5,
        'name': 'Xiaomi Black Shark 4s',
        'price': 255000000,
        'image':'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-black-shark-5.png'
    }]

    if kw:
        prd = [p for p in prd if p['name'].find(kw)>=0]
    return prd