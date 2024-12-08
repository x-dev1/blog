from django.db import models
from django.db.models.constraints import UniqueConstraint


class Post(models.Model):
    """Модель поста."""

    name = models.CharField(
        "Название",
        max_length=256
    )
    text = models.TextField(
        'Текст поста',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    """Модель отзыва."""

    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        blank=False
    )
    email = models.EmailField(
        verbose_name='Email',
        blank=False
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        blank=False
    )
    is_approved = models.BooleanField(
        default=False,
        verbose_name='Проверено'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.full_name
