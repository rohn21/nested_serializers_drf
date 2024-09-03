from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    # author = models.ForeignKey('User', on_delete=models.CASCADE, related_name="blog")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog_post = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name="comments")
    user_name = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user_name