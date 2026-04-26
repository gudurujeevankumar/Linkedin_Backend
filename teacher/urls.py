from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('details/', views.teacher_details),
    path('insert/', views.insert, name="insert"),
    path('data/', views.all_data, name='all_teachers'),
]