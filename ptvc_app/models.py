from django.db import models
from django.urls import reverse


class Subject(models.Model):
    '''
    '''
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject


class Contact(models.Model):
    '''
    '''
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    question = models.TextField()
    answer = models.TextField()

    def get_absolute_url(self):
        return reverse('ptvc_app:question_list')

    def __str__(self):
        return (self.question)[:20] + '...'


class Day(models.Model):
    '''
    '''
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.day


class Employee(models.Model):
    '''
    '''
    name = models.CharField(max_length=50)
    expertise = models.ManyToManyField(Subject)
    days = models.ManyToManyField(Day)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default="me@plastictree.com")
    phone = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
