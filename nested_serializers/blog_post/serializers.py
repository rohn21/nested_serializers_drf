from rest_framework import serializers
from blog_post.models import Blog, Comment
        
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog_post', 'content', 'user_name', 'created_at', 'updated_at']
        
        def create(self, validated_data):
            blog_post_id = self.context['view'].kwargs.get('blog_post_id')
            blog_post = Blog.objects.get(id=blog_post_id)
            validated_data['blog'] = blog_post
            return super().create(validated_data)
        
        def update(self, instance, validated_data):
            blog_post_id = self.context['view'].kwargs.get('blog_post_id')
            blog_post = Blog.objects.get(pk=blog_post_id)
            instance.blog_post = blog_post
            instance.content = validated_data.get('content', instance.content)
            instance.user_name = validated_data.get('user_name', instance.user_name)
            instance.save()
            return instance            

# class CreateBlogSerializer(serializers.ModelSerializer):    
#     class Meta:
#         model = Blog
#         fields = ['id', 'title', 'description', 'author', 'created_at', 'updated_at']
                    
class BlogSerializer(serializers.ModelSerializer):    
    comments = CommentsSerializer(many=True, required=False, read_only=False)
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'author', 'created_at', 'updated_at', 'comments']
        
    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])
        blog = Blog.objects.create(**validated_data)
        for comment in comments_data:
            Comment.objects.create(blog_post=blog, **comment)
        return blog

    def update(self, instance, validated_data):
        comments_data = validated_data.pop('comments', [])
        
        existing_comments = instance.comments.all()
        
        existing_comments_data = { comments.id: comments for comments in existing_comments }
        
        for comments in comments_data:
            comment_id = comments.get('id')
            if comment_id:
                existing_comment = existing_comments_data.get(comment_id)
                if existing_comment:
                    existing_comment.content = comments.get('content', existing_comment.content)
                    existing_comment.user_name = comments.get('user_name', existing_comment.user_name)
                    existing_comment.save()
                else:
                    Comment.objects.create(blog_post=instance, **comments) 
            else:
                Comment.objects.create(blog_post=instance, **comments)
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        
        # for comments in comments_data:
        #     comment_id = comments.get('id')
        #     if comment_id and comment_id in existing_comment_ids:
        #         get_comment = Comment.objects.get(id=comment_id, blog_post=instance)
        #         get_comment.content = comments.get('content', get_comment.content)
        #         get_comment.user_name = comments.get('user_name', get_comment.user_name)
        #         get_comment.save()
        #     else:
        #         Comment.objects.create(blog_post=instance, **comments)

        return instance
                
        
        
# class BlogDetailSerializer(serializers.ModelSerializer):
#     comments = CommentsSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = Blog
#         fields = ['id', 'title', 'description', 'author', 'created_at', 'updated_at', 'comments']
        
