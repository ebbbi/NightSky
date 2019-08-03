from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, todayemotion
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.core import serializers
import json
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
 

    #def post_edit(request, index):
     #   post = get_object_or_404(Post, pk=index)
      #  if request.method == "POST":
       #     form = PostForm(request.POST, instance=post)
        #    if form.is_valid():
         #       post = form.save(commit=False)
          #      post.author = request.user
           #     post.pub_date = timezone.now()
            #    post.save()
             #   return redirect('post_detail', index=post.pk)
           # else:
            #    form = PostForm(instance=post)
        #return render(request, {'form': form})

def post_edit(request):
    if request.method=="GET":
        pk=request.GET['pk']
        post=get_object_or_404(Post, pk=pk)
        context={'body': post.body, 'date': post.pub_date, 'pk':pk}
        return JsonResponse(context)
    elif request.method=="POST":
        pk=request.POST['pk']
        post=get_object_or_404(Post, pk=pk)
        post.body=request.POST['content']
        post.save()
        return HttpResponse()

def post_delete(request):
    if request.method=="GET":
        pk=request.GET['pk']
        post=get_object_or_404(Post, pk=pk)
        post.delete()
        return HttpResponse()
        #author = request.user
        #posts = Post.objects.filter(author=request.user).order_by('-pub_date')
        #return render(request, 'main/mysky.html', {'posts': posts})
      
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
    if request.method=="POST":
        author=request.user
        body=request.POST['body']
        emotion=request.POST['emo']
        lng=request.POST['x']
        lat=request.POST['y']
        image=request.POST['im']
        pub_date=timezone.now()
        Post.objects.create(author=author, body=body, emotion=emotion, lng=lng, lat=lat, image=image, pub_date=pub_date)
    
        return redirect('mysky')
    elif request.method=="GET":
        return render(request, 'main/mysky.html', {'posts':posts})
   # if request.method == 'POST':
    #    form = PostForm(request.POST, request.FILES)
     #   if form.is_valid():
      #      post = form.save(commit=False)
       #     post.author=request.user
        #    post.lng=request.POST['x']
         #   post.lat=request.POST['y']
          #  post.save()
           # return redirect('mysky')
    #else:
     #   form = PostForm()
    #return render(request, 'main/mysky.html', {'posts':posts, 'form':form})

def realmain(request):
    if request.method=="POST":
        em=request.POST['emo']
        posts=Post.objects.filter(emotion=em)
        today=todayemotion.objects.filter(author=request.user)
        if today:
            today=todayemotion.objects.get(author=request.user)
            today.emotion=em
            today.save()
        else:
            author=request.user
            emotion=em
            todayemotion.objects.create(author=author, emotion=emotion)
        return render(request, 'main/realmain.html', {'posts':posts})
    else:
        today=todayemotion.objects.get(author=request.user)
        em=today.emotion
        posts=Post.objects.filter(emotion=em)
        return render(request, 'main/realmain.html', {'posts':posts})

def user_update(request):
        user=get_object_or_404(User, username=request.user.username)
        return render(request, 'main/user_update.html', {'user':user})
def change_Email(request):
        if request.method=="POST":
                newemail=request.POST['NEWEMAIL']
                user=get_object_or_404(User, username=request.user.username)
                user.email=newemail
                user.save()
                #return render(request, 'user_update.html', {'message3':'※이메일이 변경되었습니다.'})
                return redirect('user_update')
def change_ID(request):
        if request.method=="POST":
                newID=request.POST['NEWID']
                if User.objects.filter(username=newID).exists():
                    return render(request, 'main/user_update.html', {'message4':'※이미 사용중인 ID입니다.'})
                else:
                    user=User.objects.get(username=request.user.username)
                    user.username=newID
                    user.save()
                    auth.logout(request)
                    return redirect('home')

def change_pw(request):
    if request.method == "POST":
        current_password = request.POST['origin']
        user = User.objects.get(username=request.user.username)
        if check_password(current_password, user.password):
            new_password = request.POST['password1']
            password_confirm = request.POST['password2']
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.logout(request)
                return redirect('home')
            else:
                return render(request, 'main/user_update.html', {'message2':'※비밀번호가 일치하지 않습니다.'})
        else:
                return render(request, 'main/user_update.html', {'message':'※원래 비밀번호가 아닙니다.'})

def mysearch(request):
    if request.method=="POST":
        word=request.POST['word']
        post=Post.objects.filter(author=request.user)&(Post.objects.filter(body__icontains=word)|Post.objects.filter(emotion__icontains=word))
        return render(request, 'main/mysky.html', {'posts':post})

def postdetail(request, index):
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
        return render(request, 'main/mysky.html', {'form':form, 'postdetail':post, 'comments':comments})