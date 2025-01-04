from django.shortcuts import render, get_object_or_404
from .models import Forum
from thread.models import Thread


def index(request):
    forums = Forum.objects.all()
    return render(request, 'index.html', {'forums': forums})


def forum_detail(request, slug):
    forum = get_object_or_404(Forum, slug=slug)
    threads = Thread.objects.filter(forum=forum).order_by('-created_at')
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'threads': threads})
