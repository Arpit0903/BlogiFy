from django.urls import path
# from . import views
from .views import HomeView, ArticleView, AddBlogView, UpdateBlogView, DeleteBlogView, MyBlogsView, LikeView, UserBlogsView

urlpatterns = [
    # path('', views.index, name = 'index')
    path('', HomeView.as_view(), name = 'home'),
    path('article/<int:pk>/', ArticleView.as_view(), name = 'article_detail'),
    path('user/<str:username>/', UserBlogsView.as_view(), name='user_posts'),
    path('my_blogs/', MyBlogsView.as_view(), name = 'my_blogs'),
    path('add_post/', AddBlogView.as_view(), name = 'add_blog'),
    path('article/edit/<int:pk>', UpdateBlogView.as_view(), name = 'update_blog'),
    path('article/delete/<int:pk>', DeleteBlogView.as_view(), name = 'delete_blog'),
    path('like/<int:pk>/', LikeView, name = 'like_post'),
    # path('article/<int:pk>/comment', add_comment, name = 'add_comment')
]