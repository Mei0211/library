"""studentmanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from app01 import views as App_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', include("app01.urls")),
    path('login/',App_views.login),
    path('register/',App_views.register),
    path('search_book/',App_views.search_book),
    path('login_judge/', App_views.login_judge),
    path("add_publisher/", App_views.add_publisher),
    path("publisher_list/", App_views.publisher_list),
    path("edit_publisher/", App_views.edit_publisher),
    path("delete_publisher/", App_views.delete_publisher),
    path("book_list/", App_views.book_list),
    path("add_book/", App_views.add_book),
    path("edit_book/", App_views.edit_book),
    path("delete_book/", App_views.delete_book),
    path("author_list/", App_views.author_list),
    path("add_author/", App_views.add_author),
    path("edit_author/", App_views.edit_author),
    path("delete_author/", App_views.delete_author),
    path('',App_views.login),
]
