from rest_framework import serializers
from .models import User
#새로 생성한 User로 연결

class UserSerializer(serializers.ModelSerializer):
    #회원가입
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['nickname', 'email', 'name', 'password']