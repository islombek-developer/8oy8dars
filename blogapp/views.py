from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Comment,Food,FoodType
from .serializers import FoodTypeSerializers,FoodSerializers,CommentSerializers
from rest_framework.authentication import  BasicAuthentication,SessionAuthentication,TokenAuthentication
from .permissins import CastomPermission

class FoodView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [CastomPermission]
    authentication_classes = [TokenAuthentication]

class FoodTypeView(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializers
    permission_classes = [CastomPermission]
    authentication_classes = [BasicAuthentication,SessionAuthentication]

class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [CastomPermission]
    authentication_classes = [BasicAuthentication,SessionAuthentication]
