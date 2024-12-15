from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.loginView,name="login"),
    path("varify/",views.VarifyView,name="varify"),
    path("saveContact/",views.saveContactView,name="saveContact"),

    
]
