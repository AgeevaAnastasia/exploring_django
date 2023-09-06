from django.contrib import admin

from .models import Author, Post


class AuthorAdmin(admin.ModelAdmin):
    """Автор"""
    list_display = ['name', 'lastname', 'email']
    list_filter = ['birthdate', 'lastname']
    search_fields = ['name', 'lastname', 'bio']
    search_help_text = 'Поиск по полю Описание продукта (description)'

    """Отдельный продукт."""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['birthdate']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'lastname'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание автора',
                'fields': ['bio', 'birthdate'],
            },
        ),
    ]


class PostAdmin(admin.ModelAdmin):
    """Пост"""
    list_display = ['title', 'author']
    search_fields = ['title', 'author', 'content']
    search_help_text = 'Поиск по полю название, автор, контент'

    """Отдельный продукт."""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['public_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание статьи',
                'fields': ['content', 'category', 'views'],
            },
        ),
    ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
