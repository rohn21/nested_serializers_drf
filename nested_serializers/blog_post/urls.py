from django.urls import path
from .views import BlogCreateListView, CommentCreateView, BlogDetailView, CommentUpdateView

urlpatterns = [
    path('blogs/', BlogCreateListView.as_view(), name="create-list-blog"),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name="detail-blog"),
    path('blogs/<int:blog_post_id>/comment/', CommentCreateView.as_view(), name="create-comment"),
    path('blogs/<int:blog_post_id>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name="update-comment")
]
