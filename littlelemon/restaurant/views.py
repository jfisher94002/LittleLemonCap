from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking, Menu
from .serializers import (BookingSerializer, MenuItemSerializer,
                          MenuSerializer, UserSerializer)

# Create your views here.


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})


def index(request):
    return render(request, "index.html", {})


class MenuItemsView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
