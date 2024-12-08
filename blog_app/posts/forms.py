from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """Создание формы для отзывов."""

    class Meta:
        model = Review
        fields = ['full_name', 'email', 'text']
        help_texts = {
            'full_name': 'Ваше ФИО',
            'email': 'Email',
            'text': 'Текст отзыва'
        }
