from rest_framework import serializers
from apps.plans.models import Plan

class PlanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = [
            'id', 
            'code', 
            'name', 
            'price', 
            'billing_cycle', 
            'currency',
            'active', 
            'created_by'
        ]
        # fields = "__all__"
    
    def validate_code(self, value):
        if Plan.objects.filter(code=value).exists():
            raise serializers.ValidationError(
                "Plan with this code already exists."
            )
        return value

    def validate_price(self, value):
        if value <=0:
            raise serializers.ValidationError(
                "Price must be greater than zero."
            )
        return value
    
    def validate(self, attrs):
        if attrs["billing_cycle"] == 'yearly' and attrs["price"] < 10:
            raise serializers.ValidationError(
                "Yearly plans must have a minimum price of 10."
            )
        return attrs

class PlanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = [
            "name",
            "price",
            "billing_cycle",
            "currency",
            "active",
        ]
    
    def validate_price(self, value):
        if value <=0:
            raise serializers.ValidationError(
                "Price must be greater than zero."
            )
        return value

class PlanReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = [
            "id",
            "code",
            "name",
            "price",
            "billing_cycle",
            "currency",
            "active",
            "created_at",
            "updated_at",
        ]