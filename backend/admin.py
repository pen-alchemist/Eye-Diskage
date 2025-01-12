from django.contrib import admin

from backend.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"post_slug": ("post_title",)}
    list_display = ('post_title', 'post_slug', 'created_date')
    search_fields = ('post_title', 'post_content')
    ordering = ('-created_date',)
    date_hierarchy = 'created_date'

admin.site.register(BlogPost, BlogPostAdmin)
