from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework_csv.renderers import CSVRenderer

from .serializers import UserSerializer
from .models import User

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user_id": user.id,
            "username": user.username,
            "token": token.key,
        })

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

class UserXSLXView(XLSXFileMixin, generics.ListAPIView):
    serializer_class = UserSerializer
    renderer_classes = [XLSXRenderer]
    queryset = User.objects.all()
    filename = 'users.xlsx'
    xlsx_ignore_headers = ["password"]

class UserCSVVIew(generics.ListAPIView):
    serializer_class = UserSerializer
    renderer_classes = [CSVRenderer]
    queryset = User.objects.all()
    pagination_class = None
    filename = 'my_export.csv'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response['Content-Disposition'] = 'attachment; filename="users.csv'
        return response