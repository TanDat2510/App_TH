from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from App import App, db
from App.models import Category,Products


admin = Admin(app=App, name='Quản Trị Bán Hàng', template_mode='bootstrap4')


class MyproductView(ModelView):
    column_display_pk = True
    column_list = ['name','price','category']
    column_searchable_list = ['name']
    column_filters = ['name','price']
    can_export = True
    can_view_details = True


class MyCategoryView(ModelView):
    column_list = ['name','products']



class MyStatsView(BaseView):
    @expose("/")
    def __index__(self):
        return self.render('admin/stats.html')


admin.add_view(MyCategoryView(Category,db.session))
admin.add_view(MyproductView(Products,db.session))
admin.add_view(MyStatsView(name='Thống Kê Báo Cáo'))