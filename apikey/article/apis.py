from rest_framework.response import Response
from rest_framework.views import APIView
from apikey.article.serializers import InputArticleSerializer, OutputArticleSerializer
from apikey.article.use_cases.services import create_article


class CreateArticleAPIView(APIView):
    def post(self, request):
        serializer = InputArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        body = serializer.validated_data.get('body')
        article = create_article(title, body)
        return Response(data=OutputArticleSerializer(article).data, status=201)

