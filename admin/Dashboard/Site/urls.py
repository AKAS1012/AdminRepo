from django.conf.urls import url
from . import views

app_name = 'Site'

urlpatterns = [
    url(r'^post/$', views.Posts.as_view(), name="post"),
    url(r'^post/$', views.Posts.as_view(), name="post"),
]

