from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thankyou", views.ThankYouView.as_view(),name="thankyou"),
    path("reviews",views.ReviewsListView.as_view(), name="reviews"),
    path("reviews/<int:pk>",views.SingleReviewView.as_view())
]