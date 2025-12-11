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

# is het niet riskant om de id mee te geven via een url om te verwijderen?
# Waarom moet je bij 'check' een id mee geven?  
# Je schreef al een update, waarom dan nog een userUpdateWw? 