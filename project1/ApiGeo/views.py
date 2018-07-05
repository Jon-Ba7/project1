from django.shortcuts import render
import requests
import re

from music.models import Album
from stock.serializers import AlbumSerializer
from rest_framework import generics, filters
####
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response



def index(request):
    search = request.GET['search']
    context = {
        'search': search
    }
    return render(request, 'ApiGeo/index.html')


'''
def index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        context = {
            'search': search
        }
        url = 'http://127.0.0.1:8000/stock/'
        response = requests.get(url)
        search_result = response.json()
        p = re.compile(search, re.IGNORECASE)
        d = {'k': []}
        """
        if search in search_result:
            d['val'] = search
            return render(request, 'core/home2.html', d)
        """
        for r in search_result:
            if p.match(r['artist']):
                d['k'].append(r['artist'])
                #d[r['id']] = r['artist']
                return render(request, 'ApiGeo/index.html', context)

    #return render(request, 'core/home2.html')
    return render(request, 'ApiGeo/index.html')


'''



class FilterListView(generics.ListAPIView):
    queryset = Album.objects.all().filter(artist = "Taylor Swift")
    #queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (filters.OrderingFilter,)
    filter_fields = ('artist')
    ordering_fields = ('artist','id')


def git(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'core/github.html', {'search_result': search_result})



def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': 1,#geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyC68MXKBttY-pAMdwotJ4npNuZh7dF4AOw'  # Don't do this! This is just an example. Secure your keys properly.
    })

"""
@api_view(['GET', 'POST'])
def index(request):
    
     #   List all code snippets, or create a new snippet.
    
    if request.method == 'GET':
        snippets = Album.objects.all()
        serializer = AlbumSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""