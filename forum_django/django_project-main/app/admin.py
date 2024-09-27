from django.contrib import admin
from .models import Thread, Post, Comment, UserProfile

admin.site.register(Post)
admin.site.register(UserProfile)