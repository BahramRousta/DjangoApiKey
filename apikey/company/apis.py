from rest_framework.response import Response
from rest_framework.views import APIView
from apikey.company.serializers import InputCompanySerializer, OutputCompanySerializer
from apikey.company.use_cases.services import create_company


class CreateCompanyAPIView(APIView):

    def post(self, request):
        serializer = InputCompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company_name = serializer.validated_data.get('name')
        new_company = create_company(company_name)
        return Response(data=OutputCompanySerializer(new_company).data, status=201)