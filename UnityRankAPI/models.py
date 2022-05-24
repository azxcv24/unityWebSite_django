from django.db import models
from Users.models import User

# Create your models here.
#pk는 따로 안해도 자동으로 생성
class GameRank(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    playTime = models.TimeField(null=False)
    deathCount = models.IntegerField(null=False)
    gameVersion = models.CharField(max_length=10)
    createdTime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['createdTime'] #정렬기준듯