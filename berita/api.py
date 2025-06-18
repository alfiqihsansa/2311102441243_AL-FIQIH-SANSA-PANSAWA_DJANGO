from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from berita.serializers import BiodataSerializer, KategoriSerializer, ArtikelSerializer
from berita.models import Kategori, Artikel
from pengguna.models import Biodata

@api_view(['GET'])
def api_author_list(request):
    biodata = Biodata.objects.all()
    serializer = BiodataSerializer(biodata, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_kategori_list(request):
    kategori = Kategori.objects.all()
    serializer = KategoriSerializer(kategori, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
def api_kategori_detail(request, id_kategori):
    try:
        kategori = Kategori.objects.get(id=id_kategori)
    except:
        return Response({'message:data kategori ditemukan'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":

        serializer = KategoriSerializer(kategori, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = KategoriSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:pass

@api_view(['POST'])
def api_kategori_add(request):
    serializer = KategoriSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_artikel_list(request):
    key_token = "157a17b99b32bdaa8e1c901a2982751c817fa904b9a55e401df53cfaea2b7e0e"
    token = request.headers.get('token')
    if token == None:
        return Response({'message:masukkan token'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if token != key_token:
            return Response({'message:masukkan token yang benar'}, status=status.HTTP_401_UNAUTHORIZED)
    
    artiekl = Artikel.objects.all()
    serializer = ArtikelSerializer (artiekl, many=True)
    data = {
        'count': artikel.count(),
        'rows':serializer.data
    }
    return Response(data)

@api_view(['GET','PUT','DELETE'])
def api_artikel_detail(request, id_artikel):
    try:
        artikel = Artikel.objects.get(id=id_artikel)
    except:
        return Response({'message:data artikel ditemukan'}, status=status.HTTP_404_NOT_FOUND)
    if request.method.status == "GET":
        serializer = ArtikelSerializer(artikel, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArtikelSerializer(artikel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        artikel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def api_artikel_add(request):
    serializer = ArtikelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)