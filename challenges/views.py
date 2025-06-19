from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

# def january(request):
#     return HttpResponse("This works")

# def february(request):
#     return HttpResponse("Work for at least 20 minutes every day")


monthly_challenges_list = {
    "january": "january : This works",
    "february": "february : Work for at least 20 minutes every day",
    "march": "march : Learn Django for 30 minutes every day!",
    "april": "april : Read a book for 30 minutes every day",
    "may": "may : Practice coding for 1 hour every day",
    "june": "june : Exercise for at least 30 minutes every day",
    "july": "july : Learn a new programming language",
    "august": "august : Contribute to an open-source project",
    "september": "september : Attend a workshop or seminar",
    "october": "october : Start a personal project",
    "november": "november : Reflect on your goals and achievements",
    "december": "december : Plan for the upcoming year"
}


def index(request):
  list_items = ""
  months = list(monthly_challenges_list.keys())

  for month in months:
        print(month)
        capitalized_month = month.capitalize()
        month_path = reverse("path-name", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"  

  response_data = f"<ul>{list_items}</ul>"
  return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months =list(monthly_challenges_list.keys())

    if month < 1 or month > len(months):
        return HttpResponseNotFound("404 : Invalid month")
    redirect_month = months[month-1]  # Convert month number to month name

    redirect_url = reverse("path-name", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challenges(request,month):
    try:
         challenge_text = monthly_challenges_list[month]
         return HttpResponse(challenge_text)
    except:
         return HttpResponseNotFound("404 : This month is not supported")

 
  

     
 



