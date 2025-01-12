from django.shortcuts import render, get_object_or_404
from .models import Forum
from post.models import Post
from thread.models import Thread
from django.db.models import Max, Count


def index(request):
    forums = Forum.objects.all().annotate(
        thread_count=Count('threads', distinct=True),
        post_count=Count('threads__posts', distinct=True),
        latest_post_time=Max('threads__posts__created_at')
    )
    latest_posts = {}
    for forum in forums:
        latest_post = Post.objects.filter(
            thread__forum=forum
        ).order_by('-created_at').first()
        latest_posts[forum.id] = latest_post
    return render(request, 'index.html', {'forums': forums, 'latest_posts': latest_posts})


def forum_detail(request, slug):
    forum = get_object_or_404(Forum, slug=slug)
    threads = Thread.objects.filter(forum=forum).order_by('-created_at')
    latest_post = Post.objects.filter(
        thread__forum=forum).order_by('-created_at').first()
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'threads': threads, 'latest_post': latest_post})
