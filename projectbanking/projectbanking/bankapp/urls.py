from  . import views
from django.urls import path

urlpatterns =[

    path('', views.demo, name='demo'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('new', views.new, name='new'),
    path('form', views.form, name='form'),
    path('submit', views.submit, name='submit')

]