from django.shortcuts import render, get_object_or_404, redirect

from .forms import ReviewForm
from .models import Post, Review


def index(request):
    """Вью-функция для главной страницы."""

    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'posts/index.html', context)


def about(request):
    """Вью-функция для страницы 'о нас'."""

    return render(request, 'posts/about.html')


def post_detail(request, post_id):
    """Вью-функция для карточки авто."""

    post = get_object_or_404(Post, id=post_id)
    context = {
        "post": post
    }
    return render(request, 'posts/post_detail.html', context)


def review_list(request):
    """Вью-функция для страницы с отзывами."""

    approved_reviews = Review.objects.filter(is_approved=True)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:review_list')

    context = {
        'reviews': approved_reviews,
        'form': form,
    }
    return render(request, 'posts/review_list.html', context)
