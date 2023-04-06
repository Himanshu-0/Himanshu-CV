"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Himanshu Portfolio Admin Portal"
admin.site.index_title = "Welcome to Portfolio Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('education/',views.edu,name="edu"),
    path('experience/',views.exp,name="exp"),
    path('skills/',views.skill,name="skill"),
    path('certification/',views.certi,name="certi"),
    path('project/',views.project,name="project"),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('home.urls')),
#     path('about/',include('about_me.urls')),
#     path('contact/',include('hire.html')),
#     path('education/',include('education.html')),
#     path('experience/',include('experience.html')),
#     path('skills/',include('skills.html')),
#     path('certification/',include('certification.html')),
#     path('project/',include('project.html')),
# ]

