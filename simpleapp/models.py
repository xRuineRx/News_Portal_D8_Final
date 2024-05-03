from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User





# class Material(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class ProductMaterial(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     material = models.ForeignKey(Material, on_delete=models.CASCADE)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ranking_mark = models.IntegerField(default = 0)

class Category(models.Model):
    name = models.CharField(max_length= 100, unique = True)

    def __str__(self):
        return self.name.title()


class News_All(models.Model):

    news = 'Нов'
    article = 'Ст'

    CHOICE_MAIN = [
        (news, 'Новости'),
        (article, 'Статья'),
    ]

    news_or_art = models.CharField(max_length=3,choices = CHOICE_MAIN, default = news)

    name = models.CharField(max_length= 100, unique = True)
    text = models.TextField(max_length= 100)
    time_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name.title()}"

    def get_absolute_url(self):
        return reverse('news_or_art_detail', args=[str(self.id)])
