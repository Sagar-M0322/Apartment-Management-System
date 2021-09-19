from django.db import models
import datetime

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profilepic = models.ImageField(upload_to='img/', blank=True)
    shortintro = models.CharField(max_length=200, blank=True)


class Meta:
    db_table = "login"


CHO_CHOICE = (
    ('owner', 'OWNER'),
    ('tenent', 'TENENT'),
)


class homowner(models.Model):
    name = models.CharField(max_length=20)
    phono = models.IntegerField()
    flat = models.CharField(max_length=10)
    emailid = models.EmailField()
    Type = models.CharField(max_length=10, choices=CHO_CHOICE, default='owner')


class Meta:
    db_table = "homowner"


Cat_Choice = (('electricity', 'ELECTRICITY'), ('water', 'WATER'),
              ('cleaning', 'CLEANING'), ('lift', 'LIFT'), ('security', 'SECURITY'))


class expense(models.Model):
    category = models.CharField(
        max_length=20, choices=Cat_Choice, default='electricity')
    company = models.CharField(max_length=20)
    amount = models.IntegerField()
    tranid = models.CharField(max_length=20)
    bildate = models.DateField(default=datetime.date.today)


class Meta:
    db_table = "expense"


class income(models.Model):
    typeo = models.CharField(
        max_length=20, choices=Cat_Choice, default='electricity')
    payer = models.CharField(max_length=20)
    amount = models.IntegerField()
    tranid = models.CharField(max_length=20)
    bildate = models.DateField(default=datetime.date.today)


class Meta:
    db_table = "income"


class compaint(models.Model):
    uid = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    reason = models.TextField(max_length=100)
    dt = models.DateField(default=datetime.date.today)


class Meta:
    db_table = "compaint"


class homowndet(models.Model):
    flatNo = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    dob = models.DateField(default=datetime.date.today)
    occupation = models.CharField(max_length=20)
    comm_address = models.CharField(max_length=100)
    perm_address = models.CharField(max_length=100)
    idproof = models.FileField(default="null")
    CommAddProof = models.FileField(default="null")
    PermAddProof = models.FileField(default="null")
    SaleDeed = models.FileField(default="null")


class Meta:
    db_table = "homowndet"


class apartment(models.Model):
    aptno = models.CharField(max_length=10)
    area = models.IntegerField()
    Bathroom = models.IntegerField()
    Bedroom = models.IntegerField()
    parking = models.IntegerField()
    regMonth = models.CharField(max_length=10)


class Meta:
    db_table = "apartment"


class Maint(models.Model):
    usid = models.CharField(max_length=10, default="null")
    mon = models.DateField(default=datetime.date.today)
    trans = models.CharField(max_length=10)
    amount = models.IntegerField()


class Meta:
    db_table = "Maint"
