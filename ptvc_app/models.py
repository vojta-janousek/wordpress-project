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
