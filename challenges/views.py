from django.http import HttpResponse , HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def january(request):
    return HttpResponse("This works")

def february(request):
    return HttpResponse("Work for at least 20 minutes every day")

def march(request):
    return HttpResponse("Learn D jango for 30 minutes every day!")

def monthly_challenges(request, id):
    challenge_text = None
    if id == "1":
        challenge_text = "This works"
    elif id == "2":
        challenge_text = "Work for at least 20 minutes every day"
    elif id == "3":
        challenge_text = "Learn D jango for 30 minutes every day!"
    else:
        return HttpResponseNotFound("this month is not supported")
    return HttpResponse(challenge_text)

 
  

     
 



