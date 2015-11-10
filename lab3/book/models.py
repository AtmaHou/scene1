from django.db import models


class Author(models.Model):
    AuthorID = models.CharField(primary_key=True, max_length=30)
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)


class Book(models.Model):
    ISBN = models.CharField(primary_key=True, max_length=30)
    Title = models.CharField(max_length=30)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=30)
    PublishDate = models.CharField(max_length=30)
    Price = models.CharField(max_length=30)


