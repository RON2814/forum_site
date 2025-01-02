from django.shortcuts import render, red
from .models import Thread

# Create your views here.
def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'posts/thread_lists.html', {'threads': threads})

def create_thread(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'posts/create_thread.html')