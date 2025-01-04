from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from thread.models import Thread

# Create your views here.


def create_post(request, slug):
    if not request.user.is_authenticated:
        return redirect('login')
    thread = get_object_or_404(Thread, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        # Use id for slug uniqueness
        post = Post.objects.create(
            thread=thread,
            author=request.user,
            body=body,
        )
        post.slug = f"posts-{post.id}"
        post.save()
        return redirect('thread_page', slug=slug)
    return render(request, "post/create_post.html")
