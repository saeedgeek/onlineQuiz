from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    text=models.CharField(max_length=300)
    Asn1=models.CharField(max_length=200)
    Asn2=models.CharField(max_length=200)
    Asn3=models.CharField(max_length=200)
    Asn4=models.CharField(max_length=200)
    TrueAns=models.IntegerField()
    user=models.ManyToManyField(User,through="UserTest")


class UserTest(models.Model):
    tst=models.ForeignKey(Test,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question_status=models.BooleanField(null=True)
    q_numer=models.IntegerField()