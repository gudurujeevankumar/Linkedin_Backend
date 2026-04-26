from django.urls import path
from . import views

urlpatterns = [
    path('details/',views.stu_details),
    path('insert/',views.insert,name="insert"),
    path('data/', views.all_data, name='all_data'),
]