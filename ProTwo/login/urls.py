from django.conf.urls import url
from login import views

urlpatterns = [

url(r'^$', views.login_user, name = 'login'),
url(r'^signin', views.user, name = 'user')
]
