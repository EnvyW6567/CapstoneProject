from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class webHomeViewSet(APIView):
    def get(self, request):
        return render(request, 'test.html')
