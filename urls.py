from django.urls import path
from .views import *

urlpatterns = [

    path('',signin,name='signin'),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),
    path('contact',contact,name='contact'),
    # path("register_fun/", register_fun, name="register_fun"),
    # path("login_fun/",login_fun,name='login_fun')
    path('logout',logout_user,name='logout_user'),
    path("profile_update/", profile_update, name='profile_update'),
    path('admin_login',admin_login,name='admin_login'),
    path('message', message , name='message'),
    path('see_message',see_message,name='see_message'),
    path('add_detail', add_detail,name='add_detail'),
    path('see_detail', see_detail,name='see_detail'),
    path('add_image',add_image, name='add_image'),
    path('upload_image',upload_image, name='upload_image'),
    path('see_image',see_image,name='see_image'),
    path('image_fetch',image_fetch, name='image_fetch'),
    path('admin_page',admin_page,name='admin'),
    path('see_message',see_message,name='see_message')
]