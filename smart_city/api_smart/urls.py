from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from api_smart.views import AmbienteViewSet, SensorViewSet, HistoricoViewSet, RegisterView
from api_smart.views import ImportSensorExcelView

router = DefaultRouter()
router.register(r'ambientes', AmbienteViewSet)
router.register(r'sensores', SensorViewSet)
router.register(r'historicos', HistoricoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login, gera token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/import/sensores/', ImportSensorExcelView.as_view(), name='import-sensor-excel'),
    
    # endpoint para registrar usuário
    path('api/register/', RegisterView.as_view(), name='register'),

    # APIs REST
    path('api/', include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
