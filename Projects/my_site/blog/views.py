from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import TemplateView,ListView,DetailView




# def get_date(posts):
#     return posts['date']


# def starting_page(request):
    
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/index.html",{
#         "posts_list" : latest_posts
#     })




# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request,"blog/all-posts.html",{
#         "whole_list" : all_posts
#     })


# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post,slug=slug)

#     return render(request, "blog/post-detail.html",{
#         "post": identified_post
#     })

# class StartingPageView(TemplateView):
#     template_name = "blog/index.html"
#     con


class StartingPageListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts_list" 

    def get_queryset(self):
        return Post.objects.order_by('-date')[:3]
    

class PostListView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "whole_list"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name= "post"
