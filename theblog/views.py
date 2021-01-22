from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, News
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from . import news_extractor

# Create your views here.

#def home(request):
#   return render(request,'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class NewsView(ListView):
    model = News
    template_name = 'news.html'
    title_list = news_extractor.title_list
    author_list = news_extractor.author_list
    description_list = news_extractor.description_list
    url_list = news_extractor.url_list
    for i in range(0,len(news_extractor.title_list)):
        if News.objects.filter(title=title_list[i]).exists():
            pass
        else:
            value = News(title=title_list[i], author=author_list[i], description=description_list[i], url=url_list[i])
            value.save()
            

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
    success_url = reverse_lazy('home')


