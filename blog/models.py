from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "categories"
    genre = models.CharField(max_length=70)
    description = models.CharField(max_length=70)

class Article(models.Model):
    class Meta:
        db_table = "articles"
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)

