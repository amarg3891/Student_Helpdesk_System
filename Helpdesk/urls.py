from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.log_in,name='login'),
    path('logout',views.log_out,name='logout'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('<int:pk>', views.course, name='course'),
    path('syllabus', views.syllabus, name='syllabus'),

]