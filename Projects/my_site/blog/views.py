from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.views import View
from .forms import CommentModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse


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


class PostDetailView(View):

    def get(self,request,slug):
        post = Post.objects.get(slug=slug)

        return render(request,"blog/post-detail.html",{
            "post": post,
            "comment_form":CommentModelForm(),
            "comments":post.comments.all().order_by("-id")
        })

    
    def post(self,request,slug):
        comment_form = CommentModelForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))

        return render(request,"blog/post-detail.html",{
            "post": post,
            "comment_form":comment_form,
            "comments":post.comments.all().order_by("-id")
        })

   
    
