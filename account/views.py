from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import User
from django.shortcuts import render 
from . import token
class AccountViewSet(APIView):
    def get(self, request):
        user = User.objects.all().first()
        tok = token.CreateToken(user)
        print(tok)
        return render(request, "test.html")