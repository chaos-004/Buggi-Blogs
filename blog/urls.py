from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', views.CategoryPostListView.as_view(), name='category_posts'),
    path('tag/<slug:slug>/', views.TagPostListView.as_view(), name='tag_posts'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('post/<slug:slug>/comment/', views.AddCommentView.as_view(), name='add_comment'),
]
