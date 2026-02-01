from rest_framework import serializers
from .models import Account, Subscription, AccountBalance

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'name', 'email', 'phone_number', 'created_at'
        ]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id', 'account', 'plan_name', 'start_date', 'end_date', 'active'
        ]


class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBalance
        fields = [
            'id', 'account', 'balance_amount', 'last_updated'
        ]