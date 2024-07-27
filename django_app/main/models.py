from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    """Модель пункта меню"""
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    title = models.CharField(max_length=100, verbose_name='Название')
    url = models.CharField(max_length=255, verbose_name='Ссылка')
    named_url = models.CharField(max_length=255, blank=True, verbose_name='Имя ссылки')
    menu_name = models.CharField(max_length=255, verbose_name='Название пункта меню')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reverse(self.named_url)
        return '/#'