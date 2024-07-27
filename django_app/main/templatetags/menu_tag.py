from django import template
from django.urls import reverse

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu_list.html', takes_context=True)
def show_top_menu(context):
    menu_items = MenuItem.objects.all()
    return {
        "menu_items": menu_items,
    }


