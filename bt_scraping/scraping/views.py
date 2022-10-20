from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scraping.serializers.bt_serializer import BTSerializer
from scraping.services.scraper_service import scrap_BT

@api_view(['POST'])
def bt_scraping(request):
    if request.method == 'POST':
        # get the data by scraping
        bt_data = scrap_BT()
        # save it to DB
        for data in bt_data:
            data = {'name': data[0], 'value': data[1]}
            bt_serializer = BTSerializer(data=data)
            if bt_serializer.is_valid():
                bt_serializer.save()
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
