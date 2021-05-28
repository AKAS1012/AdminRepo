from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Socialmedia.apps'

urlpatterns = [
    url(r'^dashboard/$', views.Dashboard.as_view(), name="dashboard"),
    url(r'^dashboard/home/$', views.Home.as_view(), name="Home"),
    url(r'^dashboard/update/$', views.Update.as_view(), name="update")

]
