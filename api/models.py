from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    # number of rates for each meal
    def no_of_rates(self):
        rates = Rating.objects.filter(meal = self)
        return len(rates)

    # average of the rates for each meal
    def avg_of_rates(self):
        sum = 0
        rates = Rating.objects.filter(meal=self)
        for rate in rates:
            sum += rate.stars
        if len(rates) > 0:
            return sum / len(rates)
        else:
            return 0

    def __str__(self):
        return self.title

class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    # def __str__(self):
    #     return self.meal

    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)