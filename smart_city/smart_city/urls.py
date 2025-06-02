from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from api_smart.views import AmbienteViewSet, SensorViewSet, HistoricoViewSet, RegisterView
from api_smart.utils import importar_excel_sensor, importar_excel_historico, importar_excel_ambientes







from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_smart.views import AmbienteViewSet, SensorViewSet, HistoricoViewSet, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'ambientes', AmbienteViewSet)
router.register(r'sensores', SensorViewSet)
router.register(r'historicos', HistoricoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login, gera token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/import/sensores/', importar_excel_sensor, name='import-sensor-excel'),
    path('api/import/historico/', importar_excel_historico, name='import-ambientes-excel'),
    
    
    # endpoint para registrar usuário
    path('api/register/', RegisterView.as_view(), name='register'),

    # APIs REST

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
