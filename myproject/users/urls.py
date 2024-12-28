from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ForgotPasswordAPIView, DisplayUsersAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot_password'),
    path('user-data/', DisplayUsersAPIView.as_view(), name='user_data'),
]
