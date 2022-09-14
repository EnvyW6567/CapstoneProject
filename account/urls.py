from django.urls import path
from rest_framework.authtoken import views # Token 
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "account"

urlpatterns = [
    path('',views.AccountViewSet.as_view(),name="account"),
    # path('login', views.LoginViewSet.as_view(), name="login"),
    # path('logout', views.LogoutViewSet.as_view(), name="logout"),
    # path('signin', views.SigninViewSet.as_view(), name="signin"),
    # path('find-email', views.FindEmailViewSet.as_view(), name="find-email"),
    # path('find-password', views.FindPasswordViewSet.as_view(), name="find-password"),
    path('api-token-auth/', obtain_auth_token)
]