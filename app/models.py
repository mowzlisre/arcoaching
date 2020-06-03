from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    answer = models.TextField()
    def __str__(self):
        return self.question
    

class Test(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question)
    time = models.SmallIntegerField()
    date = models.DateField(("Date"), default=date.today)
    description = models.TextField()
    students = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.subject
    
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    choices = models.TextField(blank=True)
    marklist = models.TextField(blank=True)
    marks = models.IntegerField(blank=True)