from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post
from .forms import PostCreationForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


def PostDetail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
        'title': 'Post Details'
        }
    return render(request, 'posts/detail.html', context)

def create_post(request):
    form = PostCreationForm()

    if request.method == 'POST':
        form = PostCreationForm(request.POST)

        if form.is_valid():
            form_obj = form.save(commit=False)

            form_obj.author = request.user
            form_obj.save()

            return redirect(reverse('homepage'))

    
    context = {'form': form}
    return render(request, 'posts/create-post.html', context)