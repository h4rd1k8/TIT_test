from api.models import RubricList, Rubric, Author, News
from api.serializers import RubricSerializer, RubricListSerializer, AuthorSerializer, NewsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

class RubricListsAPIView(generics.ListCreateAPIView):
    serializer_class = RubricListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return RubricList.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class RubricListAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RubricListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return RubricList.objects.for_user(user=self.request.user)


class RubricListNewsAPIView(generics.ListCreateAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            rubric_list = RubricList.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except RubricList.DoesNotExist:
            raise Http404
        return rubric_list.task_set.all()

    def perform_create(self, serializer):
        try:
            rubric_list = RubricList.objects.get(id=self.kwargs['pk'])
        except RubricList.DoesNotExist:
            raise Http404
        serializer.save(rubric_list=rubric_list)
