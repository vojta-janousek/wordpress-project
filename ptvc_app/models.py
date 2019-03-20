from django.db import models


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

    def __str__(self):
        return (self.question)[:20] + '...'
