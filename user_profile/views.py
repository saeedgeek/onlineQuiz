from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# Create your views here.
class register_user(APIView):
    def post(self,request):
        data=request.data
        check_format=UserSerializer(data=request.data)
        if check_format.is_valid():
            if User.objects.filter(username=check_format.data["username"]).exists():
                return Response({"message","user is exist please login"},status=401)
            else:
                username=check_format.validated_data.get('username')
                password=check_format.validated_data.get('password')
                email=check_format.validated_data.get('email')
                user=User.objects.create_user(username=username,email=email,password=str(password))
                user.save() 
                return Response({"stsus":"ok",
                    "msg":"user "+check_format.data["username"]+" register successFully"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class login_user(APIView):
    def post(self,request):
        data=request.data
        serializer = UserSerializer(data=data)

        if (serializer.is_valid()):
            username=serializer.validated_data.get('username')
            password=serializer.validated_data.get('password')
            if User.objects.filter(username=serializer.data["username"]).exists():
                user=authenticate(username=username,password=password)
                token,statr=Token.objects.get_or_create(user=user)
                return Response({"token":"Token "+token.key})
            else:
                return Response({"status":"bad",
                "msg":"user is not valid please register first"})



        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

