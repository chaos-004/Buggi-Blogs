from django.contrib import admin
from .models import Category, Post, Comment, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at', 'published_at')
    list_filter = ('status', 'category', 'created_at', 'published_at')
    search_fields = ('title', 'content', 'summary')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'summary', 'content')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Publishing', {
            'fields': ('status', 'published_at', 'featured_image')
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"
