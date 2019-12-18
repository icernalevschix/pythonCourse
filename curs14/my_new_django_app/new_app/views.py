from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from datetime import datetime
from random import randint
import os
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_first_view(request):

    answers = {}
    answers['ex1'] = str(datetime.now())
    answers['ex2'] = randint(1,50000)
    answers['ex3'] = str(datetime(2020, 1, 1) - datetime.now())
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