from . import views
from django.urls import path
app_name = 'movieapp'

urlpatterns = [
    path('',views.movies,name= 'movies'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('addmovies',views.add_movies,name='addmovies')
    

]