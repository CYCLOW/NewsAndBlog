from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,new
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
import json
import requests

title_list = []
author_list = []
description_list = []
url_list = []

api_key = "ce469d5428b34c429269bb781eedb119"

urlx = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(api_key)

response = requests.get(urlx)
news_json = json.loads(response.text)

count = 5 # Number of news to read.

for news in news_json['articles']:
    if count >=0 :
        title = str(news['title'])
        author = str(news['author'])
        description = str(news['description'])
        url = str(news['url'])

        title_list.append(title)
        author_list.append(author)
        description_list.append(description)
        url_list.append(url)
        count -= 1

for i in range(0,len(title_list)):
    if new.title == title_list[i]:
        pass
    else:
        value = new(title=title_list[i], author=author_list[i], description=description_list[i], urls=url_list[i])
        value.save()
# Create your views here.

#def home(request):
#   return render(request,'home.html', {})

class NewsView(ListView):
    model = new
    template_name = 'news.html'

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
            

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home_blogs')


