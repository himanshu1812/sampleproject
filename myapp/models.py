from django.db import models
import datetime as d
from django.shortcuts import reverse

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.TextField()
    studentimage = models.ImageField(upload_to="studentimage",null=True)

    def get_absolute_url(self):
        return reverse("show")

class  Lib(models.Model):
	CHOICES = (
        ('11', 'A'),
        ('12', 'B'),
        ('13', 'C'),
        ('21', 'D'),
        ('22', 'E'),
        ('31', 'F'),
        ('32', 'G'),
    )
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	book = models.CharField(choices = CHOICES,max_length=50)
	issue_date = models.DateField(default=d.datetime.today)
