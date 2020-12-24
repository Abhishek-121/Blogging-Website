from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    # path('details/<slug:slug>', views.blog_details, name='blog_details'),
]
