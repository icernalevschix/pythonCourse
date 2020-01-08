from django.shortcuts import render
from . import models


def home(request):
    context = {
        'posts': models.Post.objects.all()
    }

    return render(request, 'job_list/home.html', context)

def about(request):
    return render(request, 'job_list/about.html')

# class home(models.Post):
#     class meta:
