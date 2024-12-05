from django.shortcuts import render

def home(request):
    return render(request, 'App_22_3/home.html')

def about(request):
    return render(request, 'App_22_3/about.html')

def projects(request):
    return render(request, 'App_22_3/projects.html')

def contact(request):
    return render(request, 'App_22_3/contact.html')
