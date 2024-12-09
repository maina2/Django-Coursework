from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.starting_page , name="starting-page"),
#     path("posts", views.posts, name="posts-page"),
#     path("posts/<slug:slug>",views.post_detail, name="post-detail-page")
# ]

urlpatterns = [
    path("", views.StartingPageListView.as_view() , name="starting-page"),
    path("posts", views.PostListView.as_view(), name="posts-page"),
    path("posts/<slug:slug>",views.PostDetailView.as_view(), name="post-detail-page")
]