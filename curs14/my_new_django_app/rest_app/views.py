from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from rest_app.serializers import FancyCatSerializer, FluffyTigerSerializer, FluffyTigerAllSerializer
from rest_app.models import FancyCat, FluffyTiger
from rest_app.permissions import AllowGetMethod

class FancyCatListView(APIView):

    permission_classes = ( AllowGetMethod, )
    # authentication_classes = (TokenAuthentication, )

    def get(self, request, format=None):
        fancy_cats = FancyCat.objects.all()
        serializer = FancyCatSerializer(fancy_cats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FancyCatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FancyCatDetailView(APIView):

    # permission_classes = ( AllowGetMethod, )

    def get_object(self, pk):
        try:
            return FancyCat.objects.get(pk=pk)
        except FancyCat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fancy_cat = self.get_object(pk)
        serializer = FancyCatSerializer(fancy_cat)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fancy_cat = self.get_object(pk)
        serializer = FancyCatSerializer(fancy_cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fancy_cat = self.get_object(pk)
        fancy_cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FluffyTigerListView(APIView):

    permission_classes = ( AllowGetMethod, )

    def get(self, request, format=None):
        fluffy_tigers = FluffyTiger.objects.all()
        serializer = FluffyTigerSerializer(fluffy_tigers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FluffyTigerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FluffyTigerListAllView(APIView):

    permission_classes = ( AllowGetMethod, )

    def get_object(self, pk):
        try:
            return FluffyTiger.objects.get(pk=pk)
        except FluffyTiger.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fluffy_tiger = self.get_object(pk)
        serializer = FluffyTigerAllSerializer(fluffy_tiger)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fluffy_tiger = self.get_object(pk)
        serializer = FluffyTigerAllSerializer(fluffy_tiger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fluffy_tiger = self.get_object(pk)
        fluffy_tiger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)