# define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = "restaurant"

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuItemsView.as_view(), name="menu"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("menu/items", views.MenuItemsView.as_view()),
    path("menu-items/", views.MenuItemsView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    path("message/", views.msg),
    path("api-token-auth/", obtain_auth_token),
]
