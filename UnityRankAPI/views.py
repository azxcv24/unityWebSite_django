#프레임워크
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
#데어터 처리
from .models import GameRank
from .serializers import GameRankSerializer


# Create your views here.
#GET,POST 부분
class GameRankListAPI(APIView):
    
    #TODO 페이징 기능 추가
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
            serializer.save() #저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#하나씩 조회
class GameRankDetailAPI(APIView):
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


    '''
    #수정기능(불필요)
    def put(self, request, pk, format=None):
        gameRankObject = self.get_object(pk)
        serializer = GameRankSerializer(gameRankObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
    #삭제(불필요)
    def delete(self, request, pk, format= None):
        gameRankObject =  self.get_object(pk)
        gameRankObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''
#뷰에서 get과 post
@csrf_exempt
def gamerank_list(request):
    if request.method == 'GET':
        query_set = GameRank.objects.all()
        serializer = GameRankSerializer(query_set, many = True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GameRankSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def gameranks(request, pk):
    obj = GameRank.objects.get(pk = pk)

    if request.method == 'GET':
        serializer =GameRankSerializer(obj)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GameRankSerializer(obj,data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE' :
        obj.delete()
        return HttpResponse(status=204)
'''