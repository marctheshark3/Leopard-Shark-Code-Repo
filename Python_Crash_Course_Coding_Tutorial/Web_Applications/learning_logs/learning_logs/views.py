from django.shortcuts import render

# Create your views here.
def index(request):
    """The hope page for Learning Log"""
    return render(request, 'learning_logs/index.html')