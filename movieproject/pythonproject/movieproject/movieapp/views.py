from django.shortcuts import render
from .models import Movies

# Create your views here.

def movies(request):
    movie = Movies.objects.all()
    return render(request,'index.html',{'movies' : movie})
def details(request,movie_id):
    movies = Movies.objects.get(id=movie_id)
    return render(request,'details.html',{'movies': movies})
def add_movies(request):
    if request.method == 'POST':
        movie = request.POST['moviename']
        year = request.POST['year']
        des = request.POST['des']
        image = request.FILES['image']
        movies = Movies(movie= movie,year=year,des=des,image=image)
        movies.save()

    return render(request,'addmovies.html')
     
