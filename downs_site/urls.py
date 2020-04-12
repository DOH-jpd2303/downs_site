"""downs_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from welcome import views as welcome_views
from blog import views as blog_views
from projects import views as projects_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_views.home_view, name='home'),
    path('blog/', blog_views.blog_view, name="blog"),
    path('projects/', projects_views.projects_main_view, name="projects"),
    path('projects/tribute', projects_views.projects_tribute_page, name="tribute"),
    path('projects/survey', projects_views.projects_survey_page, name="survey"),
    path('projects/product', projects_views.projects_product_page, name="product"),
    path('projects/techdoc', projects_views.projects_techdoc_page, name="techdoc")
]
