from django.urls import path
from .views import my_view

urlpatterns = [
    path('my-url/', my_view, name='your_view_name'),
]