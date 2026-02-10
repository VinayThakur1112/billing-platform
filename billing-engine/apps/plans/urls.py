from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PlanCreateView,
    PlanListView,
    PlanDetailView,
    PlanViewSet,
)


# router = DefaultRouter()
# router.register(
#     r"plans", PlanViewSet, basename="plan"
# )

urlpatterns = [
    path("", PlanListView.as_view(), name="plan-list"),
    path("create/", PlanCreateView.as_view(), name="plan-create"),
    # path("update/<uuid:plan_id>/", PlanDetailView.as_view(), name="plan-update"),
    path("<uuid:plan_id>/", PlanDetailView.as_view(), name="plan-detail"),
]