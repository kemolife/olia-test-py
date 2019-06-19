from django.contrib import admin
from .models import Post, Settings, Category, Tag, Comment

admin.site.register(Post)
admin.site.register(Settings)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)