from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from serial.serializers import studentserializer
from serial.models import student


class HelloApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'number0fyear': 10,
        }

        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
