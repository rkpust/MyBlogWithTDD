from django.shortcuts import render
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
    context = {'form': form}
    return render(request, 'posts/create-post.html', context)