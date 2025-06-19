from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,),  # pass static url
    path("<int:month>", views.monthly_challenges_by_number), #pass dynamic url
    path("<str:month>", views.monthly_challenges, name="path-name"), #pass dynamic url to the view

]