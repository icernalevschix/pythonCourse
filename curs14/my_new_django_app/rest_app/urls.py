from django.urls import path
from rest_framework.authtoken import views as rest_views
from . import views

urlpatterns = [
    path('fancy-cats/', views.FancyCatListView.as_view(), name='fancy_cats_list'),
    path('fancy-cats/<int:pk>/', views.FancyCatDetailView.as_view(), name='fancy_cats_detail'),
    path('api-token-auth/', rest_views.obtain_auth_token),

    path('fluffy-tigers/', views.FluffyTigerListView.as_view(), name='fluffy_tigers_list'),
    path('fluffy-tiger/<int:pk>/', views.FluffyTigerListAllView.as_view(), name='fluffy_tiger'),

]