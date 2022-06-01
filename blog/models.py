from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = 'my_category'
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=256)

class Article(models.Model):
    class Meta:
        db_table = 'my_article'
    title = models.CharField(max_length=70)
    content = models.TextField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
