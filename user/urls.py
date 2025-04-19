from django.urls import path
from .google import GoogleLoginView
from .views import (
    RegisterUser, 
    UserList, 
    LoginUser, 
    LogoutUser, 
    UserDetails, 
    RequestPasswordReset, 
    VerifyOTP, 
    ResetPassword
)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetails.as_view(), name='user-details'),
    path('request-password-reset/', RequestPasswordReset.as_view(), name='request-password-reset'),
    path('verify-otp/', VerifyOTP.as_view(), name='verify-otp'),
    path('reset-password/', ResetPassword.as_view(), name='reset-password'),
    path('auth-google/', GoogleLoginView.as_view(), name='auth-google'),
]
