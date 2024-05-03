from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
# Create your models here.
#Всего 5 моделей: Author,Category,Post,PostCategory,Comment.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ranking_mark = models.IntegerField(default = 0)
    
    def update_rating(self):

        posts_rating = Post.objects.filter(link_Author = self).aggregate(pr = Coalesce(Sum('ranking_mark'), 0))['pr']
        comments_rating = Comment.objects.filter(link_Post_User_com=self.user).aggregate(cr = Coalesce(Sum('ranking_mark'), 0))['cr']
        posts_comments_rating = Comment.objects.filter(link_Post_news_or_art__link_Author = self).aggregate(pcr = Coalesce(Sum('ranking_mark'), 0))['pcr']



        self.ranking_mark = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()
class Category(models.Model):
    category_field = models.TextField(unique = True)

class Post(models.Model):

    link_Author = models.ForeignKey(Author, on_delete=models.CASCADE)

    news = 'Нов'
    article = 'Ст'

    CHOICE_MAIN = [
        (news, 'Новости'),
        (article, 'Статья'),
    ]

    news_or_art = models.CharField(max_length=3,choices = CHOICE_MAIN, default = news)
    time_in = models.DateTimeField(auto_now_add=True)
    link_PostCategory = models.ManyToManyField(Category, through = "PostCategory")
    news_or_art_name = models.CharField(max_length = 50)
    news_or_art_text = models.TextField()
    ranking_mark = models.IntegerField(default = 0)


    def like(self):
        self.ranking_mark = self.ranking_mark + 1
        self.save()


    def dislike(self):
        self.ranking_mark = self.ranking_mark - 1
        self.save()

    def preview(self):
        return self.news_or_art_text[0:124] + "..."

class PostCategory(models.Model):
    #otm = OneToMany
    link_otm_Post_1 = models.ForeignKey(Category, on_delete=models.CASCADE)
    link_otm_Post_2 = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    link_Post_news_or_art = models.ForeignKey(Post,on_delete=models.CASCADE)
    link_Post_User_com = models.ForeignKey(User, on_delete=models.CASCADE)
    text_com = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    ranking_mark = models.IntegerField(default = 0)

    def like(self):
        self.ranking_mark = self.ranking_mark + 1
        self.save()


    def dislike(self):
        self.ranking_mark = self.ranking_mark - 1
        self.save()