from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PlanViewSet, PlanCreateView)


router = DefaultRouter()
router.register(
    r"plans", PlanViewSet, basename="plan"
)

urlpatterns = [
    path("plans/create/", 
         PlanCreateView.as_view(), # Converts the class into a callable view function
         name="plan-create"),
    path("", include(router.urls)),
]