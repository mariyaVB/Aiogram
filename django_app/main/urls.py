import django.urls
from django.urls import path
import main.views as menu

urlpatterns = [
    path('', menu.MenuItemView.as_view(), name='menus'),
]
