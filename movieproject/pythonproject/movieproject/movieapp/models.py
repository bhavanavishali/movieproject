from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    c_name=models.CharField(max_length=150,unique=True)
    description=models.TextField()
    def __str__(self) -> str:
        return self.c_name
    
class Movies(models.Model):

    movie = models.CharField(max_length=100)
    des = models.TextField()
    release_date = models.DateField(null=True)
    actors = models.CharField(max_length=255,null=True)
    youtube_trailer = models.URLField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    year=models.IntegerField()
    image = models.ImageField(upload_to='poster', blank=True, null=True)

    def __str__(self) -> str:
        return self.movie


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    location=models.CharField(max_length=120,null=True)
    phone=models.IntegerField(null=True)
    def __str__(self) -> str:
        return self.user.username
    
class Review(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.movie} "
    
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    rating=models.IntegerField()
    def __str__(self) -> str:
        return f"Rating by {self.user.username} on {self.movie.movie} "

    



