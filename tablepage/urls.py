from django.urls import re_path
from tablepage import views

urlpatterns = [
    re_path(r'^$', views.table),
    re_path(r'^page/(\d+)/$', views.table),
]
