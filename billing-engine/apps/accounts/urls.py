from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (AccountViewSet, 
                    SubscriptionViewSet, 
                    AccountBalanceViewSet)


router = DefaultRouter()
router.register(
    r"accounts", AccountViewSet, basename="account"
)
router.register(
    r"subscriptions", SubscriptionViewSet, basename="subscription"
)
router.register(
    r"account-balance", AccountBalanceViewSet, basename="account-balance"
)

urlpatterns = [
    path("", include(router.urls)),
]