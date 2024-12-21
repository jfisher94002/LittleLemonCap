from django.shortcuts import render
import rest_framework  # Add this import
from rest_framework import generics, viewsets, permissions 
from .models import Menu, Booking 
from .serializers import MenuSerializer, BookingSerializer, UserSerializer 
from django.contrib.auth.models import User

# Create your views here.
def index(request):
   return render(request, 'index.html', {})
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 