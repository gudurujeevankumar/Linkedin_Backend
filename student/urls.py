from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert, name="insert"),
    path('data/', views.all_data, name='all_data'),
    path('update/<int:id>/', views.update_stu, name='update_stu'),
    path('delete/<int:id>/', views.delete_stu, name='delete_stu'),
]