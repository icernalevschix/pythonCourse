from django.urls import path
from . import views

urlpatterns = [
    path('ex1', views.my_first_view),
    path('ex2', views.my_second_view),
    path('posts/2003/', views.special_case_2003),
    path('posts/<int:year>/', views.year_archive),
    path('posts/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/',views.article_detail),
    path('my-cat/', views.cat_image_view),
    path('json-response/', views.json_view),
    path('streaming-response/', views.streaming_view),
    path('recent-posts/', views.recent_blog_posts, name='blog_posts'),
    path('blog-post/<int:blog_post_id>/', views.blog_post_view, name='blog-detail'),
    path('add-blog/', views.add_blog_post, name='add-blog'),
    path('edit-blog/<int:blog_post_id>/', views.edit_blog_post, name='edit-blog'),

]