from flask import render_template, request
import dao
from App import App


@App.route("/")
def index():
    kw = request.args.get('kw')
    cates = dao.get_categorites()
    products = dao.load_products(kw=kw)
    return render_template("index.html", categorites=cates, prd=products)
@App.route("/products/<id>")
def details(id):
    return render_template("details.html")
if __name__ == '__main__' :
    App.run(debug=True)