from app.views import TodoViewSet

from rest_framework.routers import DefaultRouter #Faz todas as urls necessárias

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls