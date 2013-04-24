# Create your views here.

from django.http import  HttpResponse





def movie(request, movie_id):
    return HttpResponse("<h1>Hola Mundo, Star Wars </h1>" + movie_id  )


