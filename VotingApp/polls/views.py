from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo. Você está na index da aplicação polls.")
