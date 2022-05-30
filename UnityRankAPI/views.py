from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
#데어터 처리
from .models import GameRank
from .serializers import GameRankSerializer

#페이징
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page_size'
    #max_page_size = 100


class GameRankViewSet(viewsets.ModelViewSet):
    # authentication(인증방식)), permission 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] #작성시 로그인필요

    queryset = GameRank.objects.all().order_by("playTime", "deathCount");
    serializer_class = GameRankSerializer
    pagination_class = LargeResultsSetPagination
    #필터 설정
    #filter_backends = [DjangoFilterBackend, OrderingFilter]
    #filterset_fields = ['user', 'createdTime', 'gameVersion']
    #ordering_fields = ['playTime']

    #serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(user = self.request.user) #user정보 저장

'''
####APIView를 활용한 방식
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

class GameRankListAPI(APIView):
    # authentication, permission 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #list로 보여줄떄
    def get(self, request):
        gameRankList = GameRank.objects.all() #질의할 쿼리생성
        print(gameRankList)
        serializer = GameRankSerializer(gameRankList, many=True)
        return Response(serializer.data)
    
    #새로운 랭킹 작성
    def post(self, request):
        serializer = GameRankSerializer(data = request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save(user=self.request.user) #저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameRankDetailAPI(APIView):
    # authentication, permission 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #해당 객체 가져오기
    def get_object(self, pk):
        try:
            return GameRank.objects.get(pk=pk)
        except GameRank.DoesNotExist:
            raise Http404

    #가저온 객체를 이용 출력
    def get(self, request, pk, format=None):
        gameRankObject = self.get_object(pk)
        serializer = GameRankSerializer(gameRankObject)
        return Response(serializer.data)



    #수정기능(불필요)
    def put(self, request, pk, format=None):
        gameRankObject = self.get_object(pk)
        serializer = GameRankSerializer(gameRankObject, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #삭제(불필요)
    def delete(self, request, pk, format= None):
        gameRankObject =  self.get_object(pk)
        gameRankObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
