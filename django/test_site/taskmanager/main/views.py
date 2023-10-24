from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})

