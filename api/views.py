from rest_framework import viewsets
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class RatingViewSet(viewsets.ModelViewset):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer