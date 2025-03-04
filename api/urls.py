from django.urls import path,include
from .views import get_products, create_product
from .views import hello_world
from rest_framework.routers import DefaultRouter  # ✅ Import DefaultRouter
from .views import TaskViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse
from django.contrib import admin

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

def home(request):
    return JsonResponse({"message": "Welcome to my Django API!"})



urlpatterns = [
    path('products/', get_products, name='get_products'),
    path('products/create/', create_product, name='create_product'),
    path('hello/', hello_world, name='hello-world'),
    path('', include(router.urls)),  # Include router-generated URLs
    path('api/', include(router.urls)),  # Ensure 'api/' is in the path
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', home),  # Add this for the root route
    #path('api/', include('api.urls')),  # Your API routes
    path('admin/', admin.site.urls),
    



]
