from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api_parse_data.urls',namespace='api')),
    path('auth/', include('farpost.auth_urls',namespace='auth')),

]
