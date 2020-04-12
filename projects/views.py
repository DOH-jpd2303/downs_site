from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def projects_main_view(request):
    return render(request, "projects/projects_main.html")

def projects_tribute_page(request):
    return render(request, "projects/tribute.html")

def projects_survey_page(request):
    return render(request, "projects/survey.html")

def projects_product_page(request):
    return render(request, "projects/product.html")

def projects_techdoc_page(request):
    return render(request, "projects/techdoc.html")
