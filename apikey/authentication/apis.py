from rest_framework.response import Response
from rest_framework.views import APIView
from apikey.authentication.serializers import InputApiKeySerializer, OutputApiKeySerializer
from apikey.authentication.use_cases.services import create_api_key


class CreateApiKeyAPIView(APIView):
    def post(self, request):
        serializer = InputApiKeySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company_id = serializer.validated_data.get('company_id')
        api_key = create_api_key(company_id)
        return Response(data=OutputApiKeySerializer(api_key).data, status=201)