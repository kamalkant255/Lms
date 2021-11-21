from django.contrib import admin
from django.urls import path,include
from website.views import HomePageView,MyCoursesList,coursepage,SignupView,LoginView,signout,checkout,verifyPayment
from .models import *
from django.conf.urls.static import static
from course.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('logout',signout,name='logout'),
    path('my-courses',MyCoursesList.as_view(),name='my-courses'),
    path('signup',SignupView.as_view(),name='signup'),
    path('login',LoginView.as_view(),name='login'),
    path('course/<str:slug>',coursepage,name='coursepage'),
    path('check-out/<str:slug>',checkout,name='check-out'),
    path('verify_payment',verifyPayment,name='verify_payment'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(MEDIA_URL,document_root=MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
