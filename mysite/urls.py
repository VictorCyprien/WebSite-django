"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from lycee import views
from lycee.views import CursusCallView, PresenceCreateView, StudentCreateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('lycee/', views.home, name='home'),
    path('lycee/<int:cursus_id>', views.detail_grade, name='detail_grade'),
    path('lycee/teacher/<int:teacher_id>', views.detail_teacher, name='detail_teacher'),
    path('lycee/student/<int:student_id>', views.detail_student, name='detail_student'),
    path('lycee/student/create', login_required(StudentCreateView.as_view()), name='create_student'),
    path('lycee/student/update/<int:student_id>', login_required(views.update_student), name='update_student'),
    path('lycee/cursuscall/<int:cursus_id>', views.cursus_call, name='cursus_call'),
    path('lycee/presence/', views.detail_all_presence, name='detail_all_presence'),
    path('lycee/presence/create', login_required(PresenceCreateView.as_view()), name='create_presence'),
    path('lycee/presence/update/<int:presence_id>', login_required(views.update_presence), name='update_presence'),
    path('lycee/presence/<int:presence_id>', views.detail_presence, name='detail_presence'),
]