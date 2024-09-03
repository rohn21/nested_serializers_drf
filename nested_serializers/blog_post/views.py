from django.shortcuts import render
from rest_framework import generics
from blog_post.models import Blog, Comment
from blog_post.serializers import BlogSerializer, CommentsSerializer
# Create your views here.

class BlogCreateListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    
    # def perform_create(self, serializer):
    #     blog_post_id = self.kwargs.get('blog_post_id')
    #     blog_post = Blog.objects.get(id=blog_post_id)
    #     serializer.save(blog_post=blog_post)
    
class CommentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
