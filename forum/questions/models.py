from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):

    STATUS = (
        ('published','published'),
        ('draft', 'draft'),
    )

    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)  
    status = models.CharField(max_length=15, choices=STATUS)

    class Meta:
        unique_together = [['title', 'content']]

    
    def __str__(self):
        return f'{self.title}'






class Answer(models.Model):

    STATUS = (
        ('published','published'),
        ('draft', 'draft'),
    )

    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    content = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS)

  

    

