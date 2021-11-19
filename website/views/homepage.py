from django.shortcuts import render
from django.shortcuts import HttpResponse
from website.models import Course
from django.views.generic import ListView


class HomePageView(ListView):
    template_name="courses/home.html"
    queryset=Course.objects.filter(active=True)
    context_object_name='courses'



def home(request):
    courses=Course.objects.all()
    print(courses)


    return render(request, template_name='courses/home.html',context={"courses":courses})



    