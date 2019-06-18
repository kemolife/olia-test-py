from django.contrib import admin
from .models import Post, Settings, Category

admin.site.register(Post)
admin.site.register(Settings)
admin.site.register(Category)

