from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models

class TeamViewSet(ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
