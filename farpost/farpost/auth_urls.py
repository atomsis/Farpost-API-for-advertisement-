from django.urls import path
from dj_rest_auth.registration.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'auth'

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='auth_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]