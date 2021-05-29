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

@login_required(login_url='/login')
def mypage(request):


    return render(request, 'mypage.html')

def category(request):

    return render(request, 'category.html')

def academy(request):

    return render(request, 'academy.html')

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

    return render(request, 'lecture_detail.html')

@login_required(login_url='/login')
def academy_form(request):
    if request.method == 'POST':
            new_academy = Post.objects.create(
                title = request.POST['title'],
                content = request.POST['content'],
                apply_start = request.POST['apply_start'],
                apply_end = request.POST['apply_end'],
                category = request.POST['category'],
                logo = request.POST['logo',]
            )
            return redirect('academy', new_academy.pk)
    
    return render(request, 'academy_form.html')


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
        return redirect('lecture_detail', new_lecture.pk)

    return render(request, 'lecture_form.html')