from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, Subscription, AccountBalance
from .serializers import (AccountSerializer, 
                          SubscriptionSerializer, 
                          AccountBalanceSerializer)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class AccountBalanceViewSet(viewsets.ModelViewSet):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer