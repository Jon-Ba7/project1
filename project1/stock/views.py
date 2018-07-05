from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#from .models import Stock
from music.models import Album
from django.views.generic.edit import CreateView

from stock.models import Stock
from .serializers import StockSerializer
from .serializers import AlbumSerializer
from django.contrib.auth.decorators import login_required



# Create your views here.

# List all object or create a new
class StockList(APIView):

    def get(self, request):
        #stocks = Stock.objects.all()
        stocks = Album.objects.all()
        serializer = AlbumSerializer(stocks, many=True)

        '''
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
        '''
        return Response(serializer.data)

    def post(self, request):
            serializer = AlbumSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
