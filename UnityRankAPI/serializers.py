from rest_framework import serializers
from .models import GameRank

class GameRankSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source= 'user.nickname')
    class Meta:
        model = GameRank
        fields = ['id', 'user','playTime', 'deathCount','gameVersion' , 'createdTime']

