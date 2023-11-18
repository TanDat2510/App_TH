from flask import render_template, request
import dao
from App import App,login


@App.route("/")
def index():
    kw = request.args.get('kw')
    cates = dao.get_categorites()
    products = dao.load_products(kw=kw)
    return render_template("index.html", categorites=cates, prd=products)
@App.route("/products/<id>")
def details(id):
    return render_template("details.html")

@App.route("/admin/login",methods=['post'])
def login_admin_process():
    request.form.get('username')
    request.form.get('password')


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)
if __name__ == '__main__' :

    from App import admin
    App.run(debug=True)