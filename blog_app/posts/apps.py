from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Регистрация приложения."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
