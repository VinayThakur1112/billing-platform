# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Plan
from .serializers import (PlanSerializer)

# # Create your views here.
# class PlanViewSet(viewsets.ModelViewSet):
#     queryset = Plan.objects.all()
#     serializer_class = PlanSerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import IntegrityError

class PlanCreateView(APIView):
    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            try:
                plan = serializer.save()
                return Response(
                    PlanSerializer(plan).data,
                    status=status.HTTP_201_CREATED
                )
            except IntegrityError:
                return Response(
                    {"error": "Plan already exists."},
                    status=status.HTTP_409_CONFLICT
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)