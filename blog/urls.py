from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('author/<str:username>/', views.author_posts, name='author-posts'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post'),
    path('post/new/', views.CreatePost.as_view(), name='new-post'),
    path('comment/new/', views.comment, name='comment'),
    path('post/<int:pk>/update/', views.UpdatePost.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='delete-post'),
    path('reports/', views.reporters, name='blog-reports'),
    
]