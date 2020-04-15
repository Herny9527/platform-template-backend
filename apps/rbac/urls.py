from django.urls import path,include
from rest_framework import routers
from .views import user,role

router = routers.SimpleRouter()
router.register(r'users', user.UserViewSet)
router.register(r'roles', role.RoleViewSet,)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'auth/login/', user.UserAuthView.as_view()),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]