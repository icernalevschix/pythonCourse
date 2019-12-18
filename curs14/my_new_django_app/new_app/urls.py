from django.urls import path
from . import views

urlpatterns = [
    path('ex1', views.my_first_view),
    path('ex2', views.my_second_view),

]