from django.db import models
from datetime import date
# Create your models here.
class Course(models.Model):
    photo=models.FileField(blank=True)
    name=models.CharField(max_length=100)
    mentor=models.CharField(max_length=100)
    day_f=models.DateField(default=date.today)

    def __str__(self):
        return '%s'% self.name

cat_list=(('B','Boxing'),('C','Cycling'),('Y','Yoga'),('M','Meditation'),('G','Gym-Fitness'))
shif_list=(('M','Morning'),('E','Evening'))
class Course_Single(models.Model):
    photo=models.FileField(blank=True)
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=1,null=True,blank=True,choices=cat_list)
    mentor=models.CharField(max_length=100)
    day_f=models.DateField(default=date.today)
    day_t=models.DateField(default=date.today)
    student=models.IntegerField()
    price=models.FloatField()
    shift=models.CharField(max_length=1,null=True,blank=True,choices=shif_list)

    timing=models.FloatField()
    calo=models.FloatField()
    desc=models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return '%s'% self.name

    
