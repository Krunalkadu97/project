from django.db import models
from datetime import date
# Create your models here.
class AboutMe(models.Model):
    about_me=models.TextField(max_length=500)
    intro=models.TextField(max_length=500)
    photo=models.FileField(blank=True)

    def __str__(self):
        return '%s'% (self.about_me)


class Education(models.Model):
    name=models.CharField(max_length=30)
    speci=models.CharField(max_length=30)
    colleg=models.CharField(max_length=30)
    s_date=models.DateField(default=date.today)
    e_date=models.DateField(default=date.today)
    marks=models.FloatField()

    def __str__(self):
        return '%s'% (self.name)
j_list=(('I','Internship'),('F','Full Time'),('P','Part Time'))
class Experience(models.Model):
    name_o=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    type_j=models.CharField(max_length=1,null=True,blank=True,choices=j_list)
    s_date=models.DateField(default=date.today)
    e_date=models.DateField(default=date.today)

    def __str__(self):
        return '%s'% (self.name_o)


class Achivement(models.Model):
    name_a=models.CharField(max_length=30)
    a_date=models.DateField(default=date.today)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return '%s'% (self.name_a)
    
    
    
    
    
