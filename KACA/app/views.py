from django.shortcuts import render, redirect
from .models import Post, Post_comment, Lecture, Lecture_comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):

    return render(request, 'main.html')

def signup(request):

    return render(request, 'signup.html')

def login(request):

    return render(request, 'login.html')

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
