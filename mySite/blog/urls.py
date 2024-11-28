from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HomeView.as_view(), name='homeUrl'),
    path('bio', views.bio, name='bioUrl'),
    path('allposts', views.AllPostsView.as_view(), name='allpostsUrl'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='postDetailUrl'),
    path('posts-by-tag/<str:tag>', views.PostsByTagView.as_view(), name='postsByTagUrl'),
    path('all-posts/<str:author>', views.AuthorAllPostView.as_view(), name='authorAllPostsUrl'),
    path('author-bio/<str:authorName>', views.AuthorBioView.as_view(), name='authorBioUrl'),
    path('registraion', views.RegisterView.as_view(), name='registerURL'),
    path('login', views.LogInView.as_view(), name='loginURL')
]
