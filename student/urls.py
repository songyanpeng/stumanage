from django.contrib import admin
from django.urls import path, include, re_path

from student.views import index, add_student, delete_student, edit_student, eletive, search, login, register, logout, \
    edit_admin

urlpatterns = [
    path('', index),
    path('login/', login),
    re_path('edit_admin_user/(\d+)', edit_admin),
    path('logout/', logout),
    path('register/', register),
    path('index/', index),
    path('add/', add_student),
    re_path('delete/(\d+)', delete_student),
    re_path('edit/(\d+)', edit_student),
    # 选课
    re_path('eletive/', eletive),
    # 搜索
    re_path('search/', search),
]
