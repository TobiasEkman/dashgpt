
# Create your views here.
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, "dashboard/post_list.html", {"posts": posts})
