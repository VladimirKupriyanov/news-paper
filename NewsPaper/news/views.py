# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты


class NewsDetail(DetailView):
    model = Post
    template_name = 'piece_of_news.html'
    context_object_name = 'post'
