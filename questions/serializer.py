from rest_framework import serializers
from .models import Test,UserTest
class get_test_serializer(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields=['text','Ans1','Ans2','Ans3','Ans4']


class UserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserTest
        fields=['text','Ans1','Ans2','Ans3','Ans4']
        depth = 1
        