from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, FileResponse, JsonResponse, StreamingHttpResponse
from datetime import datetime
from random import randint
import os, time, datetime
from django.views.decorators.csrf import csrf_exempt
from .models import BlogPost
from .forms import BlogPostForm


@csrf_exempt
def my_first_view(request):

    answers = {}
    answers['ex1'] = str(datetime.datetime.now())
    answers['ex2'] = randint(1,50000)
    answers['ex3'] = str(datetime.datetime(2020, 1, 1) - datetime.datetime.now())
    answers['ex4'] = os.listdir(os.getcwd())
    answers['ex5'] = { 'scheme': request.scheme, 'path': request.path }

    return render(request, 'new_app/home.html', answers)

@csrf_exempt
def my_second_view(request):

    print(request)
    print(request.method)
    print(request.POST)
    
    try:
        with open('my_csv.csv', 'wb') as f:
            f.write(request.FILES['data'].read())
    except:
        pass

    return FileResponse(open('my_csv.csv', 'rb'))

def special_case_2003(request):
    print('2003')
    return HttpResponse("Year is 2003 - static")

def year_archive(request, year):
    print(year)
    return HttpResponse(f"Year is {year}")

def month_archive(request, year, month):
    print(year, month)
    return HttpResponse(f'Year is {year}, Month is {month}')

def article_detail(request, year, month, slug):
    print(year, month, slug)
    return HttpResponse(f'Year is {year}, Month is {month}, Slug is {slug}')

def cat_image_view(request):
    return FileResponse(open('cat.jpg', 'rb'))

def json_view(request):
    return JsonResponse({'name': 'Alice', 'age': 22})

def streaming_writer(rows):
    for row in range(rows):
        yield str(datetime.datetime.now()) + '</br>'
        time.sleep(0.5)

def streaming_view(request):
    return StreamingHttpResponse(streaming_writer(30))

def recent_blog_posts(request):
    recent_blog_posts = BlogPost.objects.order_by('-date_published')[:5] # descdendent( - date)

    return render(request, 'new_app/blog_posts.html', {'recent_blog_posts': recent_blog_posts})

def blog_post_view(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)

    return render(request, 'new_app/blog_post_page.html',{'blog_post': blog_post})

def add_blog_post(request):
    if request.method == 'GET':
        form = BlogPostForm()
        return render(request, 'new_app/add_new_post.html', { 'form': form})

    form = BlogPostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse(recent_blog_posts))
    return render(request, 'new_app/add_new_post.html', {'form': form})

def edit_blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id = blog_post_id)

    if request.method == 'POST':
        edit_form = BlogPostForm(request.POST, instance =blog_post )

        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse(blog_post_view, args = (blog_post_id, ) ))
    
    else:
        edit_form = BlogPostForm(instance =blog_post )
    
    return render(request, 'new_app/edit_blog_post.html', {'form': edit_form})


    
        

