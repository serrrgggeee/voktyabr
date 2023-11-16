import json

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from article.api.authenticatons import RequestTgGetAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from .serializers import ArticleSerializer
from article.models import Article


class ArticleAPIView(ListAPIView):
    authentication_classes = (SessionAuthentication,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = self.queryset
        year = self.request.GET.get("year")
        result = queryset.filter(chronology_date__year=year)
        return result


class ArticleAPIListView(ListAPIView):
    authentication_classes = (SessionAuthentication,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self, *args, **kwargs):
        return self.queryset

class ArticleAPIAddView(ListAPIView):
    authentication_classes = (SessionAuthentication,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self, *args, **kwargs):
        return self.queryset

@permission_classes((AllowAny, ))
class ArticleAPIAddView(APIView):
    authentication_classes = (BasicAuthentication,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid()
        try:
            serializer.save()
        except AssertionError as ex:
            pass
            # print(ex)
        return Response({'status_code': 200})



# api объявлений пользователя
class UsersAdAPIView(ListAPIView):
    authentication_classes = (SessionAuthentication, RequestTgGetAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = self.queryset
        tg_id = self.request.GET.get('tg_id', None)
        result = queryset.filter(user__tguser__tg_id=tg_id)
        return result


# поставить на публикацию объявлений api пользователя
class UsersAdShowAPIView(APIView):
    authentication_classes = (SessionAuthentication, RequestTgGetAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all()

    def get(self, request, id, *args, **kwargs):
        article = self.queryset.get(pk=id)
        article.show = True
        article.save()
        return Response({'status_code': 200})


# поставить на публикацию объявлений api пользователя
class UsersAdHideAPIView(APIView):
    authentication_classes = (SessionAuthentication, RequestTgGetAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all()

    def get(self, request, id, *args, **kwargs):
        article = self.queryset.get(pk=id)
        article.show = False
        article.save()
        return Response({'status_code': 200})