from .models import Movies,Profile,Category,Review,Rating
from django import forms
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['movie','des','year','image','actors','category','youtube_trailer']

class UserformReg(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','password','email','first_name','last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'phone']
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =['c_name','description']
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)
