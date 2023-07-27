from rest_framework.views import APIView
from .serializers import LoginInputSerializer, LoginOutputSerializer


class LoginAPIVIew(APIView):

    def post(self, request):
        pass
