"""KACA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/<int:user_pk>/', views.mypage, name='mypage'),
    path('category/', views.category, name='category'),
    path('academy/<int:post_pk>/', views.academy, name='academy'),
    path('delete_academy_comment/<int:post_pk>/<int:post_comment_pk>/', views.delete_academy_comment, name= 'delete_academy_comment'),
    path('academy_edit/<int:post_pk>/', views.academy_edit, name='academy_edit'),
    path('academy_delete/<int:post_pk>/', views.academy_delete, name='academy_delete'),
    path('lecture_main/', views.lecture_main, name='lecture_main'),
    path('lecture_detail/<int:lecture_pk>/', views.lecture_detail, name='lecture_detail'),
    path('delete_lecture_comment/<int:lecture_pk>/<int:lecture_comment_pk>/', views.delete_lecture_comment, name= 'delete_lecture_comment'),
    path('lecture_edit/<int:lecture_pk>/', views.lecture_edit, name='lecture_edit'),
    path('lecture_delete/<int:lecture_pk>/', views.lecture_delete, name='lecture_delete'),
    path('academy_form/', views.academy_form, name='academy_form'),    
    path('lecture_form/', views.lecture_form, name='lecture_form'),    
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path('scrap/', views.scrap, name="scrap")
]
