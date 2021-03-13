from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)

class Country(models.Model):
    name = models.CharField(max_length=233)

    def __str__(self):
        return self.name


class Rate(models.Model):
    rate = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return str(self.rate)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    year = models.DateField()
    poster = models.ImageField(upload_to="movies/posters")
    video = models.FileField(upload_to='movies/video')
    categories = models.ManyToManyField(Category)
    country = models.ForeignKey(Country,null=True, on_delete=models.SET_NULL)
    rate = models.OneToOneField(Rate, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.title)






