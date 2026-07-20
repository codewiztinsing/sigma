from django.shortcuts import get_object_or_404, render

from .models import Post


def news(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, 'news.html', {
        'active_page': 'news',
        'posts': posts,
    })


def news_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'news_detail.html', {
        'active_page': 'news',
        'post': post,
    })
