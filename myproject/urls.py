from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse  # 👈 Import JsonResponse for a simple homepage

# Define a simple home view function
def home(request):
    return JsonResponse({"message": "Welcome to my Django API!"})

urlpatterns = [
    path('', home, name='home'),  # 👈 Add this line for the root URL
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
