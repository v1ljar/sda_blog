from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.all_posts, name="home"),
    path("posts/create/", views.create_post, name="create_post"),
    path("posts/<int:pk>", views.post_detail, name="post_detail"),
    path("posts/<int:pk>/edit/", views.post_update, name="post_update"),
    path("posts/my_posts/", views.my_posts, name="my_posts"),
    path("posts/longer_posts/", views.longer_posts, name="longer_posts")
=======
    path("", views.PostsListView.as_view(), name="home"),
    path("posts/create/", views.PostCreateView.as_view(), name="create_post"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_update"),
>>>>>>> origin/ClassBasedViews
]
