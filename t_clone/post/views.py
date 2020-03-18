from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from django.utils import timezone

#Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the post index.")

def post_list(request):
    posts = post.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'post/post_list.html', {'posts': posts})

'''def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
'''