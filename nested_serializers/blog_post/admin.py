from django.contrib import admin
from .models import Blog, Comment
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog_title']
    
    # displays Blog_title on which user commented
    def blog_title(self, obj):
        return obj.blog_post.title
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment,CommentAdmin)