from rest_framework import serializers
from graph.models import Fund, FundValue


class BTSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    value = serializers.FloatField()
    
    def create(self, validated_data):
        fund = Fund.objects.filter(name=validated_data['name']).first()
        if not Fund.objects.filter(name=validated_data['name']).exists():
            fund = Fund.objects.create(name=validated_data['name'])
        FundValue.objects.create(value=validated_data['value'], fund=fund)
        return fund
