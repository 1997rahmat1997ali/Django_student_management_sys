from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sec(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    roll_no = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    sec = models.ForeignKey(Sec, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    add_date = models.DateField()


    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)
