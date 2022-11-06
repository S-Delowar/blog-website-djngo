from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model - Blog
class Blog(models.Model):
    auther = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'post_auther')
    blog_title = models.CharField(max_length = 300, verbose_name = 'Put a Title')
    slug = models.SlugField(max_length = 300, unique = True)
    blog_content = models.TextField(verbose_name = 'What is on your mind?')
    blog_image = models.ImageField(upload_to = 'blog_images')
    publish_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.blog_title


# Model - Comment
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name = 'commented_blog')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'commenter_user')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.comment


# Model - Likes
class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name = 'liked_blog')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'liker_user')