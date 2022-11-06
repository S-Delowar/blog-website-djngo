from django.contrib import admin
from App_Blog.models import Blog, Comment, Likes

# Register your models here.

class BlogAmin(admin.ModelAdmin):
    list_display = ['id', 'auther', 'blog_title', 'publish_date', 'blog_image']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'blog', 'comment_date']

admin.site.register(Blog, BlogAmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Likes)