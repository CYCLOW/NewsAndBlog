
from django.urls import path
#from . import views
from . import views
from django.contrib.auth import views as auth_views
from .views import HomeView ,ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, NewsView

urlpatterns = [ 

    #path('', views.home, name='home'),
    
    path('',NewsView.as_view(), name='news'),
    
    path('blog', HomeView.as_view(), name='blogs'),
    
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/remove/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    

]
