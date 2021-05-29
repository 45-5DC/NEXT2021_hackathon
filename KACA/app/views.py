from django.shortcuts import render, redirect
from .models import Post, Post_comment, Lecture, Lecture_comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    posts = Post.objects.all()
    # posts = Post.objects.filter() # 기한 설정 해야함
    lectures = Lecture.objects.all()

    return render(request, 'main.html', {'posts': posts, 'lectures': lectures})

def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'signup.html', {
                'error' : error
                })
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user)
        return redirect('main')

    return render(request, 'signup.html')

def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다.'
            return render(request, 'login.html', {
                'error' : error
                })
        auth.login(request, found_user)
        return redirect('main')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)

    return redirect('main')

def mypage(request):
    

    return render(request, 'mypage.html')

def category(request):
    posts = Post.objects.all()
    return render(request, 'category.html', {'posts': posts})

def academy(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method=='POST':
        content = request.POST['content']
        Post_comment.objects.create(
            post = post,
            content = content,
            author = request.user
        )
        return redirect('academy', post_pk)

    return render(request, 'academy.html', {'post': post})

def delete_academy_comment(request, post_pk, post_comment_pk):
    post_comment = Post_comment.objects.get(pk=post_comment_pk)
    post_comment.delete()
    return redirect('academy', post_pk)

def lecture_main(request):
    lectures = Lecture.objects.all()
    return render(request, 'lecture_main.html', {'lectures': lectures})

def lecture_detail(request, lecture_pk):
    lecture = Lecture.objects.get(pk=lecture_pk)

    if request.method=='POST':
        content = request.POST['content']
        Lecture_comment.objects.create(
            lecture=lecture,
            content=content,
            author = request.user
        )
        return redirect('lecture_detail', lecture_pk)

    return render(request, 'lecture_detail.html') , {'lecture': lecture}

def delete_lecture_comment(request, lecture_pk, lecture_comment_pk):
    lecture_comment = Lecture_comment.objects.get(pk=lecture_comment_pk)
    lecture_comment.delete()
    return redirect('lecture_detail', lecture_pk)

@login_required(login_url='/login')
def academy_form(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            introduction = request.POST['introduction'],
            apply_start = request.POST['apply_start'],
            apply_end = request.POST['apply_end'],
            category = request.POST['category'],
            target = request.POST['target'],
            logo = request.POST['logo'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('academy', new_post.pk)
    return render(request, 'academy_form.html')

def academy_edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post.pk).update(
            title = request.POST['title'],
            introduction = request.POST['introduction'],
            apply_start = request.POST['apply_start'],
            apply_end = request.POST['apply_end'],
            category = request.POST['category'],
            target = request.POST['target'],
            logo = request.POST['logo'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('academy', post_pk)
    return render(request, 'academy_edit.html', {'post': post})

def academy_delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('main')

@login_required(login_url='/login')
def lecture_form(request):
    if request.method == 'POST':
        new_lecture = Lecture.objects.create(
            title = request.POST['title'],
            introduction = request.POST['introduction'],
            price = request.POST['price'],
            construct = request.POST['construct'],
            category = request.POST['category'],
            thumbnail = request.POST['thumbnail'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('lecture_main') ##이거 고쳐야됨##

    return render(request, 'lecture_form.html')


    

def lecture_edit(request, lecture_pk):
    lecture = Lecture.objects.get(pk=lecture_pk)

    if request.method == 'POST':
        Lecture.objects.filter(pk=lecture.pk).update(
            title = request.POST['title'],
            introduction = request.POST['introduction'],
            price = request.POST['price'],
            construct = request.POST['construct'],
            category = request.POST['category'],
            thumbnail = request.POST['thumbnail'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('lecture_detail', lecture_pk)
    return render(request, 'lecture_edit.html', {'lecture': lecture})

def lecture_delete(request, lecture_pk):
    lecture = Lecture.objects.get(pk=lecture_pk)
    lecture.delete()
    return redirect('main')
