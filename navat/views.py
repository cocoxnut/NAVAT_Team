from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models

class FoodViewSet(ModelViewSet):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer
