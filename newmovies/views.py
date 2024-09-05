from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.
def movie_list(request):
    movie = Movies.objects.all()

    # we want to implement the search feature 
    movie_name = request.GET.get('movie_name')
    if movie_name != "" and movie_name is not None:
        movie_search = movie.filter(name=movie_name)

    paginator = Paginator(movie,2)
    page = request.GET.get('page')

    movie_object = paginator.get_page(page)

    return render(request, 'newmovies/index.html', {'movie_object': movie_object})

