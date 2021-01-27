from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,News
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from . import news_extractor

# Create your views here.

#def home(request):
#   return render(request,'home.html', {})

class NewsView(ListView):
    model = Post
    template_name = 'news.html'
    # for i in range(len(title_list)):
    #     if title_list(i) == News.title(i):
    #         pass
    #     else:
    #         News.objects.create(title = news_extractor.title_list[i], author = news_extractor.author_list[i], description = news_extractor.description_list[i], urls = news_extractor.url_list[i] )
    #         News.save()

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
    success_url = reverse_lazy('home')


