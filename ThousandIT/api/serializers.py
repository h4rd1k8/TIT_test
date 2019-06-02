from rest_framework import serializers
from api.models import Author, RubricList, Rubric, News
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = '__all__'

class RubricListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RubricList
        fields = '__all__'

class RubricSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    rubric_list = RubricListSerializer(required=False)

    class Meta:
        model = Rubric
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    rubric = RubricSerializer(required=False)

    class Meta:
        model = News
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.announcment = validated_data.get('announcment', instance.announcment)
        instance.text = validated_data.get('text', instance.text)
        instance.author = validated_data.get('author', instance.author)
        instance.rubric = validated_data.get('rubric', instance.rubric)

