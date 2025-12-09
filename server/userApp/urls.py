from django.urls import path
from . import views

urlpatterns = [
    path("getAll/",views.getAll),
    path("add/",views.addUser),
    path("delete/<int:id>",views.deleteUser),
    path("update/<int:id>",views.updateUser),
    path("check/<int:id>",views.controle),
    path("userUpdateWw/<int:id>",views.userWachtwoordUpdaten),
]