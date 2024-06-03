from django.contrib import admin
from .models import Movies,Profile,Category,Review,Rating
# Register your models here.
admin.site.register(Movies)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Rating)
