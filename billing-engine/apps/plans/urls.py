from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PlanCreateView,
    PlanListView,
    PlanDetailView,
    PlanViewSet,
)


router = DefaultRouter()
router.register(
    r"plans", PlanViewSet, basename="plan"
)

urlpatterns = [
    path("create/", 
         PlanCreateView.as_view(), # Converts the class into a callable view function
         name="plan-create"),
    path("<uuid:plan_id>/", PlanDetailView.as_view(), name="plan-detail"),
    path("", include(router.urls)),
]