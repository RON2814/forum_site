from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread
from post.models import Post
from forum.models import Forum
from django.utils.text import slugify
from django.http import Http404
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.


def threads_list(request):
    threads = Thread.objects.annotate(
        post_count=Count('posts')).order_by('-created_at')
    forums = Forum.objects.all()
    latest_posts = {}
    for forum in forums:
        latest_post = Post.objects.filter(
            thread__forum=forum).order_by('-created_at').first()
        latest_posts[forum.id] = latest_post
    return render(request, 'threads/threads_list.html', {'threads': threads, 'latest_posts': latest_posts})


def thread_page(request, slug):
    try:
        thread = get_object_or_404(Thread, slug=slug)
        thread.views += 1
        thread.save()
        posts = Post.objects.filter(thread=thread).order_by('created_at')
    except Thread.DoesNotExist:
        raise Http404("Thread does not exist")
    return render(request, 'threads/thread_page.html', {'thread': thread, 'posts': posts})


@login_required
def create_thread(request, forum_slug=None):
    if forum_slug:
        forum = get_object_or_404(Forum, slug=forum_slug)
    else:
        forum = None
    forums = Forum.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if forum:
            selected_forum = forum
        else:
            forum_name = request.POST.get('forum')
            selected_forum, created = Forum.objects.get_or_create(
                name=forum_name, defaults={'description': 'No description'})

        thread = Thread.objects.create(
            forum=selected_forum,
            title=title,
            body=body,
            created_by=request.user,
        )
        thread.slug = slugify(title) + '-' + str(thread.id)
        thread.save()

        return redirect('thread_page', slug=thread.slug)

    return render(request, 'threads/create_thread.html', {'forum': forum, 'forums': forums})


def edit_thread(request, slug):
    thread = Thread.objects.get(slug=slug)
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        thread.title = title
        thread.body = body
        thread.save()
        return redirect('thread_page', slug=slug)

    return render(request, 'threads/edit_thread.html', {'thread': thread})


def delete_thread(request, slug):
    thread = Thread.objects.get(slug=slug)
    if request.method == 'POST':
        thread.delete()
        return redirect('threads_list')

    return render(request, 'threads/delete_thread.html', {'thread': thread})
