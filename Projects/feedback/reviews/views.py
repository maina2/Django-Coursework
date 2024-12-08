from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import  ReviewForm
from django.views import View
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView



# Create your views here.

class ReviewView(FormView):
     form_class = ReviewForm
     template_name= "reviews/review.html"
     success_url = "/thankyou"

     def form_valid(self, form):
          form.save()
          return super().form_valid(form)


class ThankYouView(TemplateView):
     template_name = "reviews/thankyou.html"

     def get_context_data(self, **kwargs) -> dict[str]:
         context = super().get_context_data(**kwargs)
         context["message"] = "This is working"
         return context
     
class ReviewsListView(ListView):
     model = Review
     template_name = "reviews/reviewlist.html"

     


class SingleReviewView(DetailView):
    model = Review
    template_name = "reviews/single-review.html"


class AddFavoriteView(View):
     def post(self,request):
          review_id = request.POST["review_id"]
          
          request.session["favorite_review"] = review_id

          return HttpResponseRedirect("/reviews/"+review_id)