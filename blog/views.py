from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def blog_view(request):
    return render(request, "blog/blogpost.html")
