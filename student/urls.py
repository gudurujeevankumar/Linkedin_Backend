from django.urls import path
from . import views

urlpatterns = [
    path('details/',views.stu_details),
    path('insert/',views.insert),
]