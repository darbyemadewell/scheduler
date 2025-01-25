from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from events.models import Event
from events.serializers import EventSerializer

from dateutil import parser

@api_view(['GET'])
def events_list(request):
    if request.method == 'GET':
        if(request.query_params.get('start') and request.query_params.get('end')):
            start_date = parser.isoparse(request.query_params.get('start'))
            end_date = parser.isoparse(request.query_params.get('end'))
            events = Event.objects.filter(start_time__range=[start_date, end_date])
        else:
            events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def event_detail(request):
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)