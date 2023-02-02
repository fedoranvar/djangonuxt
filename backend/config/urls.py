from claim import views as claim_views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from user import views as user_views

router = routers.DefaultRouter()

router.register(r"users", user_views.UserViewSet)
router.register(r"groups", user_views.GroupViewSet)
router.register(r"claims", claim_views.ClaimViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("login/", user_views.LoginView.as_view()),
]
