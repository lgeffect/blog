from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(req):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(req, 'blogapp/post_list.html', {'posts' : posts})
