from django.urls import path
from . import views


urlpatterns = [
    path("",views.CreateProfileView.as_view() ),
    path("users/",views.UserProfileListView.as_view())
] 
