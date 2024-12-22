from django.shortcuts import render
import rest_framework  # Add this import
from rest_framework import generics, viewsets, permissions, response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Menu, Booking, MenuItem
from .serializers import MenuSerializer, MenuItemSerializer, BookingSerializer, UserSerializer 
from django.contrib.auth.models import User

# Create your views here.

@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return response.Response({"message":"This view is protected"})

def index(request):
   return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]  # Ensure TokenAuthentication is used
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]