from django.db import models
from Users.models import User

# Create your models here.
#pk는 따로 안해도 자동으로 생성
class GameRank(models.Model):
    #userEmail = models.ForeignKey(userEmail,  on_delete=models.CASCADE)
    nickName = models.CharField(max_length=10)
    playTime = models.TimeField(null=False)
    deathCount = models.IntegerField
    gameVersion = models.CharField(max_length=10)
    createdTime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['createdTime'] #정렬기준듯

    def __str__(self):
        return self.nickName
