from rest_framework import serializers
from graph.models import Fund, FundValue


class BTSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    value = serializers.FloatField()
    
    def create(self, validated_data):
        fund = Fund.objects.filter(name=validated_data['name']).first()
        if not Fund.objects.filter(name=validated_data['name']).exists():
            fund = Fund.objects.create(name=validated_data['name'])
        if not FundValue.objects.filter(value=format(validated_data['value'], '.3f')).filter(fund_id=fund.id).exists():
            print(validated_data['value'])
            print(fund.id)
            FundValue.objects.create(value=validated_data['value'], fund=fund)   
        return fund
