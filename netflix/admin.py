from django.contrib import admin
from .models import Movie,Country,Rate, Category
# Register your models here.


class MovieInline(admin.StackedInline):
    model = Movie
    extra = 4
    max_num = 10



class CoutnryAdmin(admin.ModelAdmin):
    inlines = [MovieInline]



class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "overview", "year")
    list_filter = ("year",)

admin.site.register(Movie, MovieAdmin)

admin.site.register(Country, CoutnryAdmin)
admin.site.register(Rate)
admin.site.register(Category)
