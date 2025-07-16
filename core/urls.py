from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import login_view, logout_view, home_view, StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('api/', include(router.urls)),
]