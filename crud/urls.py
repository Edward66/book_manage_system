from django.urls import path, re_path

from crud.views import index as index_view
from crud.views import book as book_view
from crud.views import publish as publish_view
from crud.views import author as author_view
from crud.views import reg_login as other_view

urlpatterns = [

    # 首页
    re_path('^$', index_view.index, name='book'),

    # 图书
    path('add_book/', book_view.add_book, name='add_book'),
    re_path('edit/(\d+)/book', book_view.edit_book),
    re_path('delete/(\d+)/book', book_view.delete_book),

    # 出版社
    path('add_publish/', publish_view.add_publish, name='add_publish'),
    re_path('edit/(\d+)/publish', publish_view.edit_publish),
    re_path('delete/(\d+)/publish', publish_view.delete_publish),

    # 作者
    path('add_author/', author_view.add_author, name='add_author'),
    re_path('edit/(\d+)/author', author_view.edit_author),
    re_path('delete/(\d+)/author', author_view.delete_author),

    # 展示作者图书
    re_path('show_author_book/(\d+)', author_view.show_author_book),

    # 展示出版社图书
    re_path('show_publish_book/(\d+)', publish_view.show_publish_book),

    # 注册、登陆、登出页面
    path('reg/', other_view.reg, name='reg'),
    path('login/', other_view.login, name='login'),
    path('logout/', other_view.logout, name='logout'),
]
