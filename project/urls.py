from django.contrib import admin
from django.urls import path, include
from student.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
]
