from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import post
from django.utils import timezone
from .forms import PostForm


#Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the post index.")

def post_list(request):
    posts = post.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'post/post_list.html', {'posts': posts})

def post_detail(request, pk):
    posts = get_object_or_404(post, pk=pk)
    return render(request, 'post/post_detail.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})

'''def post_new(request):
    form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})
'''