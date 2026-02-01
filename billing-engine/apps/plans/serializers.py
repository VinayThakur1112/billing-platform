from rest_framework import serializers
from .models import Plan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        # fields = [
        #     'id', 'code', 'name', 'price', 'billing_cycle', 'active', 'created_at'
        # ]
        fields = "__all__"
    
    def validate_code(self, value):
        if Plan.objects.filter(code=value).exists():
            raise serializers.ValidationError(
                "Plan with this code already exists."
            )
        return value