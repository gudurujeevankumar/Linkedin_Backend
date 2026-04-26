from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('insert/', views.insert, name="insert"),
    path('data/', views.all_data, name='all_teachers'),
    path('update/<int:id>/', views.update_teach, name='update_teach'),
    path('delete/<int:id>/', views.delete_teach, name='delete_teach'),
]
