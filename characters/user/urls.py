from . import views
from django.urls import path

urlpatterns = [
    path("login/",views.userLogin,name="login"),
    path("register/",views.userRegister,name="register"),
    path("logout/",views.logout,name="logout"),
]