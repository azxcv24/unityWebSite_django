from rest_framework import serializers
from .models import GameRank

class GameRankSerializer(serializers.ModelSerializer):

    #참조키
    user = serializers.ReadOnlyField(source= 'user.nickname') #닉네임을 JSON에 출력!


    class Meta:
        model = GameRank
        fields = ['id', 'user','playTime', 'deathCount','gameVersion' , 'createdTime']

