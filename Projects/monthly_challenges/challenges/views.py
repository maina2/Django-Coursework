from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges_list = {
    "january": "Go to the gym regularly",
    "february": "Read at least one book",
    "march": "Ride a bicycle daily",
    "april": "Learn a new skill",
    "may": "Practice meditation",
    "june": "Focus on eating healthier",
    "july": "Take up a new hobby",
    "august": "Write in a journal daily",
    "september": "Go for early morning walks",
    "october": "Practice gratitude every day",
    "november": "Improve your sleep routine",
    "december": "Spend quality time with loved ones"
}

def index (request):
    list_items =""
    month_key = list(monthly_challenges_list.keys())
    for month in month_key:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items+= f"<li><a href= \"{month_path}\">{capitalized_month}<a/> "

        response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenges_int(request,month):
    month_key = list(monthly_challenges_list.keys())
    returned_month = month_key[month-1]
    redirected_path = reverse("month-challenge", args=[returned_month])
    return HttpResponseRedirect(redirected_path )



def monthly_challenges(request,month):
    
    for the_month in monthly_challenges_list:
        if the_month == month :
            return HttpResponse(monthly_challenges_list.get(month))
    else:
        return HttpResponseNotFound("404 error")

   