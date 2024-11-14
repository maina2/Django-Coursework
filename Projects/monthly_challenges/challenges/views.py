from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    month_key = list(monthly_challenges_list.keys())
  
    return render(request, "challenges/index.html",{
        "months":month_key
    })

def monthly_challenges_int(request,month):
    month_key = list(monthly_challenges_list.keys())
    returned_month = month_key[month-1]
    redirected_path = reverse("month-challenge", args=[returned_month])
    return HttpResponseRedirect(redirected_path )



def monthly_challenges(request,month):
    try:
        challenge_text = monthly_challenges_list[month]
        return render(request,"challenges/challenge.html" , {
                "text": challenge_text,
                "month_name":month
            })
    except:
        return HttpResponseNotFound("Error 404")



   