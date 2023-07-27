from rest_framework import serializers
from apikey.article.models import Article


class InputArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=255)


class OutputArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'body')