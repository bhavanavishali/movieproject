from django.shortcuts import redirect, render
from .models import Movies,Profile,Rating,Review,Category
from .forms import MovieForm,UserformReg,UserProfileForm,CategoryForm,ReviewForm,RatingForm
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# Create your views here.

def movies(request):
    movie = Movies.objects.all()
  
    return render(request,'index.html',{'movies':movie})

@login_required
def add_movies(request):
    if request.method == 'POST':
        form=MovieForm(request.POST,request.FILES,request.user)
        if form.is_valid():
            form.save()
            return redirect('movieapp:userpage')
        
    else:
        form=MovieForm()
        return render(request,'addmovies.html',{'form':form})
@login_required
def update(request,id):
    movies = Movies.objects.get(id=id)
    if movies.user != request.user:
        return redirect('/')
    if request.method == 'POST':
        form =MovieForm(request.POST or None,instance=movies)
        if form.is_valid():
            form.save()
            return redirect('movieapp:userpage')
    else:
        form = MovieForm(instance=movies)
    return render(request,'update.html',{'form':form,'movies':movies})

@login_required
def delete(request,id):
    if request.method == 'POST':
        movies=Movies.objects.get(id=id)
        movies.delete()
        return render(request,'successfull.html')
    return render(request,'delete.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        last_name = request.POST.get('last_name')
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'user name is already taken ')
                
        else:
            user = User.objects.create_user(username=username,first_name =first_name,email =email,password=password,last_name=last_name)
            user.save()
            messages.info(request,'Registeration successfully')
            return render(request,'login.html')
                
       
    return render(request,'reg.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password, is_staff=0)
        
        if user is not None:
            auth.login(request, user)
            
            # Check if the user is a staff member (admin)
            if user.is_staff:
                return render(request, 'adminlogin.html')  # Render admin template for staff members
            else:
                return redirect('movieapp:userpage')
                  # Render user template for regular users
        
        else:
            return HttpResponse('error')  # Render a template for failed login

    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

    
def searchResult(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        print(query)
        movies = Movies.objects.filter(Q(movie__icontains=query))
        print(movies)
    return render(request,'ss.html',{'movies':movies,'query':query})

def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'user_profile': profile})
def edit_profile(request,id):
    user=User.objects.get(id=id)
    form=UserformReg(request.POST or None,instance=user)
    if form.is_valid():
        form.save()
        return redirect('movieapp:profile')

    return render(request,'edit.html',{'form':form,'user':user})
@login_required
def userpage(request):
    movies = Movies.objects.all()
    user_movie=Movies.objects.filter(user=request.user)
    return render(request, 'userpage.html', {'movies': movies,'user_movie':user_movie})

def userview(request):
    users=User.objects.filter(is_staff=0)
    return render(request,'userview.html',{'user':users})
def userdelete(request,id):
    user=User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('movieapp:userview')
    return render(request,'userdelete.html')
def moviedelete(request):
    movie = Movies.objects.all()
    return render(request,'deletemovie.html',{'movie' : movie})

def categoryadd(request):

    form=CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,'adminlogin.html')
    return render(request,'categoryadd.html',{'form':form})

def movie_cat(request,c_name):
    category = get_object_or_404(Category, c_name=c_name)
    movies=Movies.objects.filter(category=category)
    return render(request,'index.html',{'movies':movies,'category':category})

def details(request,id):
    movie = Movies.objects.get(id=id)
    rating=Rating.objects.filter(movie=movie)
    review=Review.objects.filter(movie=movie)

    if request.method == 'POST':
        if 'submitt_rating' in request.POST:
            if request.user.is_authenticated:
                rating_form=RatingForm(request.POST)
                if rating_form.is_valid():
                    rating=rating_form.save(commit=False)
                    rating.movie=movie
                    rating.user=request.user
                    rating.save()
                    print("rating is submitted")
                    return redirect('movieapp:details',id=movie.id)
                
            else:
                print("pls login")
                return redirect('movieapp:login')
        if 'submitt_review' in request.POST:
            if request.user.is_authenticated:
                review_form=ReviewForm(request.POST)
                if review_form.is_valid():
                    review=review_form.save(commit=False)
                    review.movie=movie
                    review.user=request.user
                    review.save()
                    print("review is submitted")
                    return redirect('movieapp:details',id=movie.id)
                else:
                    print("pls login")
                    return redirect('movieapp:login')
    else:
        review_form=ReviewForm()
        rating_form=RatingForm()
        return render(request,'details.html',{'movie':movie,'rating':rating,'review':review,'rating_form':rating_form,'review_form':review_form})
    
    






    

