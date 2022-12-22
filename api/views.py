from rest_framework import viewsets, status
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer,UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import request
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    @action(methods='POST', detail=True)
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            """
            create or update
            """
            meal = Meal.objects.get(pk)
            user = request.user
            stars = request.data['stars']
            # username = request.data['username']
            # user = User.objects.get(username=username)
            # update
            try:
                rate = Rating.objects.get(user= user.id, meal = meal.id)
                rate.stars = stars
                rate.save()
                serializer = RatingSerializer(rate, many=False)
                json = {
                    'message': 'Meal Rate updated',
                    'result': serializer.data,
                }
                return Response(json, status=status.HTTP_202_ACCEPTED)
            # create
            except:
                rate = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rate, many=False)
                json = {
                    'message': 'Meal Rate created',
                    'result': serializer.data,
                }
                return Response(json, status=status.HTTP_202_ACCEPTED)
        else:
            json = {
                'message': 'starts are not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def update(self, request, *args, **kwargs):
        response = {
            'message': 'this is not how you should update',
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {
            'message': 'this is not how you should create',
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)