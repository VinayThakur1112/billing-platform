# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404

from apps.plans.models import Plan
from apps.plans.serializers import (
    PlanCreateSerializer,
    PlanUpdateSerializer,
    PlanReadSerializer,)


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanReadSerializer


class PlanCreateView(APIView):
    def post(self, request):
        serializer = PlanCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):   
            try:
                with transaction.atomic():
                    plan = Plan.objects.create(
                        **serializer.validated_data)
            except IntegrityError:
                return Response(
                    {"error": "Plan already exists."},
                    status=status.HTTP_409_CONFLICT
                )
        return Response(
            PlanReadSerializer(plan).data,
            status=status.HTTP_201_CREATED
        )
    

class PlanListView(APIView):
    def get(self, request):
        plans = Plan.objects.filter(
            is_active=True).order_by("created_at")
        
        serializer = PlanReadSerializer(plans, many=True)
        return Response(serializer.data)


class PlanDetailView(APIView):
    def get(self, request, plan_id):
        plan = get_object_or_404(Plan, id=plan_id)
        return Response(PlanReadSerializer(plan).data)
    
    def patch(self, request, plan_id):
        plan = get_object_or_404(Plan, id=plan_id)

        serializer = PlanUpdateSerializer(
            plan, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(PlanReadSerializer(plan).data)

    def delete(self, request, plan_id):
        plan = get_object_or_404(Plan, id=plan_id)

        plan.is_active = False
        plan.save(update_fields=["active"])

        return Response(status=status.HTTP_204_NO_CONTENT)