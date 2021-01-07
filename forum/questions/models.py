from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse



class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='برچسب')
    date_created = models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.name


class Question(models.Model):

    # STATUS = (
    #     ('published','published'),
    #     ('draft', 'draft'),
    # )

    title = models.CharField(max_length=255,  verbose_name='عنوان')
    content = RichTextField(max_length=1000, verbose_name='محتوا')
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ ویرایش')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None, verbose_name='نویسنده')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')  
    likes = models.ManyToManyField(User, blank=True, related_name='question_likes', verbose_name='رای ها')
    # dislikes = models.IntegerField(default=0)
    # status = models.CharField(max_length=15, null=True, blank=True, choices=STATUS, verbose_name='وضعیت')

    class Meta:
        unique_together = [['title', 'content']]
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.title}'

    def snippet(self):
        return self.content[:100] + '...'

    def get_absolute_url(self):    
        return reverse("questions:id", kwargs={"id": self.id}) 

    def get_like_url(self):
        return reverse("questions:like", kwargs={"id":self.id})

    def get_update_url(self):
        return reverse("questions:update", kwargs={"id":self.id})   

    def get_delete_url(self):
        return reverse("questions:delete", kwargs={"id":self.id})     
        


class Category:
    name = models.CharField(max_length=30, verbose_name='دسته بندی')
    date_created = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی ها'

class Comment:
    pass



class Answer(models.Model):

    # STATUS = (
    #     ('published','published'),
    #     ('draft', 'draft'),
    # )

    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='شناسه سوال')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    likes = models.ManyToManyField(User, blank=True, related_name='answer_likes', verbose_name='رای ها')
    content = models.TextField(verbose_name='محتوا')
    # status = models.CharField(max_length=15, choices=STATUS, verbose_name='وضعیت')

    def __str__(self):
        return self.content[:20]


    class Meta:
        verbose_name = 'پاسخ'
        verbose_name_plural = 'پاسخ ها'    
    

    def get_absolute_url(self):    
        return reverse("questions:id", kwargs={"id": self.id}) 
  
    def get_like_url(self):
        return reverse("questions:like", kwargs={"id":self.id})
    

