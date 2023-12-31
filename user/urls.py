from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from user.views import (
    UserViewSet,
    CreateUserView,
    ManageUserView,
    LogoutAPIView,
    UploadProfilePictureView,
)

router = routers.DefaultRouter()
router.register("users", UserViewSet)


urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("logout/", LogoutAPIView.as_view(), name="auth_logout"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path(
        "me/profile_picture/",
        UploadProfilePictureView.as_view(),
        name="profile_picture",
    ),
] + router.urls


app_name = "user"
