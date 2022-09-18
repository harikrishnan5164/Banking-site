from . import views
from django.urls import path


urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('forms',views.forms,name='forms'),
    path('lastpage',views.lastpage,name='lastpage')

]