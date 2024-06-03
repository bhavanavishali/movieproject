from . import views
from django.urls import path
app_name = 'movieapp'

urlpatterns = [
    
    path('',views.movies,name= 'movies'),
    path('movie/<int:id>/', views.details, name='details'),
    path('addmovies',views.add_movies,name='addmovies'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('search/',views.searchResult,name='searchResult'),
    path('userpage/',views.userpage,name='userpage'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/<int:id>',views.edit_profile,name='edit_profile'),
    path('userview/',views.userview,name='userview'),
    path('userdelete/<int:id>',views.userdelete,name='userdelete'),
    path('moviedelete/',views.moviedelete,name='moviedelete'),
    path('categoryadd/',views.categoryadd,name='categoryadd'),

    path('movie_cat/<str:c_name>/', views.movie_cat, name='movie_cat'),
    
    

]