from django.contrib import admin

from .models import Post, Review


class PostAdmin(admin.ModelAdmin):
    """Определяем поля, которые будут отображаться в админке для постов."""
    list_display = ('pk', 'name', 'text', 'image')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    """Определяем поля, которые будут отображаться в админке для отзывов."""
    list_display = ('pk', 'full_name', 'email', 'text', 'is_approved')
    search_fields = ('full_name',)
    list_editable = ('is_approved',)
    empty_value_display = '-пусто-'

admin.site.register(Post, PostAdmin)
admin.site.register(Review, ReviewAdmin)