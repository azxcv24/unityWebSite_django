from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User


class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, email, nickname, name, password=None):
        if not email:
            raise ValueError('Must have user E-mail')
        if not nickname:
            raise ValueError('Must have user NICKNAME')
        if not name:
            raise ValueError('Must have user NAME')
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 유저생성
    def create_superuser(self, email, nickname, name, password=None):
        user = self.create_user(
            email,
            password=password,
            nickname=nickname,
            name=name
        )
        user.is_admin=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)

    # 유저 모델의 필수 필드
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username 필드는 닉네임
    USERNAME_FIELD = 'nickname'

    # 필수로 작성해야하는 필드
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.nickname