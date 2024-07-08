from django.shortcuts import render
from .models import Comment,Food,FoodType
from .serializers import FoodTypeSerializers,FoodSerializers,CommentSerializers
from rest_framework.authentication import  BasicAuthentication,SessionAuthentication,TokenAuthentication


