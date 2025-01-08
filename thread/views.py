from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread
from post.models import Post
from forum.models import Forum
from django.utils.text import slugify
from django.http import Http404
from django.db.models import Count

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


def create_thread(request):
    forums = Forum.objects.all()
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        forum = Forum.objects.get(name=request.POST.get('forum'))
        title = request.POST.get('title')
        body = request.POST.get('body')
        slug = slugify(title)

        # Use id for slug uniqueness
        thread = Thread.objects.create(
            forum=forum,
            title=title,
            created_by=request.user,
            body=body,
            slug=slug
        )
        thread.slug = f"{slug}-{thread.id}"
        thread.save()
        return redirect('thread_page', slug=thread.slug)

    return render(request, 'threads/create_thread.html', {'forums': forums})


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
