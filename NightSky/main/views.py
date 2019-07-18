from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm, CommentForm
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
        if request.method =='POST':
            form=CommentForm(request.POST)
            if form.is_valid:
                comment=form.save(commit=False)
                comment.author=request.user
                comment.post=post
                comment.save()
                return redirect('post_detail', index=post.pk)
        else:
            form=CommentForm()
            comments=Comment.objects.filter(post=post)
            return render(request, 'main/post_detail.html', {'form':form, 'post':post, 'comments':comments})



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

def main(request):
    return render(request, 'main/main.html')

def comment_edit(request, index, cindex):
    comment=get_object_or_404(Comment, pk=cindex)
    post=get_object_or_404(Post, pk=index)
    if request.method=='POST':
        form=CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.save()
            return redirect('post_detail', index=post.pk)
    else:
        form=CommentForm(instance=comment)
        return render(request,'main/comment_edit.html', {'form':form })

def comment_delete(request, index, cindex):
    comment=get_object_or_404(Comment, pk=cindex)
    post=get_object_or_404(Post, pk=index)
    comment.delete()
    return redirect('post_detail', index=post.pk)

def mysky(request):
    author = request.user
    posts = Post.objects.filter(author=request.user).order_by('-pub_date')
    return render(request, 'main/mysky.html', {'posts':posts})

def realmain(request):
    if request.method=="POST":
        #em=request.POST['emo']
        #post=Post.objects.filter(emotion=em)
        #return render(request, 'realmain.html', {'post': post})
        return render(request, 'main/realmain.html')

    else:
        return render(request, 'main/realmain.html')
