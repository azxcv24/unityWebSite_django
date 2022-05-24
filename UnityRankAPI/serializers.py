from rest_framework import serializers
from .models import GameRank

class GameRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRank
        fields = '__all__'
        #fields = ('id', 'nickName','playTime','deathCount','gameVersion')

    '''
    userEmail = serializers.SerializerMethodField("get_userEmail")

    def get_userEmail(self, obj):
        return obj.userEmail
    '''