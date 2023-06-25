from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from serial.serializers import studentserializer
from serial.models import student
from rest_framework.permissions import IsAuthenticated


class HelloApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = student.objects.all()
        # student1 = qs.first() when u need only one data
        serializer = studentserializer(qs, many=True)  # (student1)pass this
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
