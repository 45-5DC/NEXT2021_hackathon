from django.shortcuts import render
from .models import Post, Comment, Lecture
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

    return render(request, 'lecture_main.html')

def lecture_detail(request):

    return render(request, 'lecture_detail.html')
