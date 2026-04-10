import random

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Parent, Student, Teacher, User
from .serializers import (
    ParentCreateSerializer,
    StudentCreateSerializer,
    TeacherCreateSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentCreateSerializer


class RequestOTPView(APIView):
    def post(self, request):
        mobile_number = request.data.get("mobile_number")
        try:
            user = User.objects.get(mobile_number=mobile_number)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        otp = random.randint(100000, 999999)
        user.otp = otp
        user.save()
        return Response({"message": "OTP sent", "otp": otp}, status=status.HTTP_200_OK)


# class VerifyOTPView(APIView):
#     def post(self, request):
#         mobile_number = request.data.get("mobile_number")
#         otp = request.data.get("otp")
#         user = User.objects.get(mobile_number=mobile_number)
