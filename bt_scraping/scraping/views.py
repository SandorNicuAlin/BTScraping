from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scraping.serializers.bt_serializer import BTSerializer
from scraping.services.scraper_service import scrap_BT


# Create your views here.

@api_view(['GET'])
def bt_scraping(request):
    if request.method == 'GET':
        bt_data = scrap_BT()
        data_to_return = []
        for data in bt_data:
            data = {'name': data[0], 'value': data[1]}
            bt_serializer = BTSerializer(data=data)
            if bt_serializer.is_valid():
                bt_serializer.save()
                data_to_return.append(data)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data_to_return)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
