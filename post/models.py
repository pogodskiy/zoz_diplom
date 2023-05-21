from django.db import models
from user.models import User

class CatPost(models.Model):
    CATEGORY_CHOICES = [
        ('health', 'Health'),
        ('meal', 'Meal'),
        ('exercise', 'Exercise'),
        ('other', 'Other'),
    ]
    name_cat = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name_cat



class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    post_body = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    comments = models.CharField(max_length=200, verbose_name='Комментарии')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    cat = models.ForeignKey(CatPost, on_delete=models.PROTECT, verbose_name='Категория', null=True)

    def __str__(self):
        return self.title

