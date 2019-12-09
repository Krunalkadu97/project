from django.db import models

# Create your models here.
class FormalShirt(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    availabel=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s'%self.name


class CasualShirt(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    availabel=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s'%self.name


class Jeans(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    availabel=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s'%self.name

class Shorts(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    availabel=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s'%self.name
    
class FormalShirt_W(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    availabel=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s'%self.name


class CasualShirt_W(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    availabel=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s'%self.name

class Jeans_W(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    availabel=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s'%self.name

class Shorts_W(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    availabel=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s'%self.name
