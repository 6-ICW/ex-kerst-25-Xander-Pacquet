from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User
import json
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def getAll(request):
    # zelf ervoor dat je telkens ook het ID mee vraag
    all_useres = User.objects.all().values("login")
    return JsonResponse(list(all_useres),safe=False)

@csrf_exempt
def addUser(request):
    # bij gebruik van defaults kan je hier wat input verminderen
    post_user = json.loads(request.body.decode("utf-8"))
    newUser = User()
    newUser.login = post_user["login"]
    newUser.password = post_user["password"]
    newUser.email = post_user["email"]
    newUser.role = post_user["role"]
    newUser.isSuperuser = post_user["isSuperuser"]
    newUser.save()
    return JsonResponse(model_to_dict(newUser),safe=False)

@csrf_exempt 
def deleteUser(request,id):
    oneUser = User.objects.get(pk=id)
    dictUser = model_to_dict(oneUser)
    oneUser.delete()
    return JsonResponse({"deleted":True, "data":dictUser})

@csrf_exempt
def updateUser(request,id):
    # je moet hier telkens een volledige user mee geven om up te daten. 
    # denk na of dit echt nodig is. 
    oneUser = User.objects.get(pk=id)
    updateData = json.loads(request.body.decode("utf-8"))
    oneUser.login = updateData["login"]
    oneUser.password = updateData["password"]
    oneUser.email = updateData["email"]
    oneUser.role = updateData["role"]
    oneUser.isSuperuser = updateData["isSuperuser"]
    oneUser.save()
    return JsonResponse(model_to_dict(oneUser),safe=False)

@csrf_exempt
def controle(request,id):
    # wat controleer je hier precies? 
    # wat doet de functie check() met het queryObject?
    oneUser = User.objects.get(pk=id).check()
    return JsonResponse(model_to_dict(oneUser),safe=False)


# deze functie werkt, maar is dus eigenlijk overbodig aangezien
# je al een andere updatefunctie schreef. 
@csrf_exempt
def userWachtwoordUpdaten(request,id):
    oneUser = User.objects.get(pk=id)
    updateData = json.loads(request.body.decode("utf-8"))
    oneUser.password = updateData["password"]
    oneUser.save()
    return JsonResponse(model_to_dict(oneUser),safe=False)
    