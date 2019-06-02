from api.models import RubricList, Rubric, Author, News
from api.serializers import RubricListSerializer, RubricSerializer, NewsSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class RubricListNewsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_news(self, request, pk1, pk2):
        try:
            news = Rubric.objects.for_user(user=request.user).get(id=pk1).news_set.get(id=pk2)
        except:
            raise Http404
        return news

    def get(self, request, pk1, pk2):
        news = self.get_news(request, pk1, pk2)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def put(self, request, pk1, pk2):
        news = self.get_news(request, pk1, pk2)
        try:
            request.data.pop('news_list')
        except:
            pass
        serializer = NewsSerializer(instance=news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk1, pk2):
        news = self.get_news(request, pk1, pk2)
        news.delete()
        return Response({"delete_status": "successful"})