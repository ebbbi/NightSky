from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all
    return render(request, "main/home.html", {'posts_list': posts})

def new(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.writer=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, {'form':form})

    def post_detail(request, index):
        post = get_object_or_404(Post, pk=index)
        return render(request, {'post': post})


    def post_edit(request, index):
        post = get_object_or_404(Post, pk=index)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.pub_date = timezone.now()
                post.save()
                return redirect('post_detail', index=post.pk)
            else:
                form = PostForm(instance=post)
        return render(request, {'form': form})


    def post_remove(request,pk):
        post=get_object_or_404(Post, pk=pk)
        post.delete()
    return redirect('post_list')
