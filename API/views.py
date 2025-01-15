from django.shortcuts import render

def index(request):
    """
    Отображает главную страницу сайта.
    """
    return render(request, 'API/index.html')