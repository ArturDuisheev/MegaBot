import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from ..services.generators.password import generate_password

from ..services.IPAddressService import get_ip, get_country_and_city


class Departament(models.Model):
    name = models.CharField(
        _('Наименование департамента'),
        max_length=120
    )
    user = models.ForeignKey(
        'EsUser',
        on_delete=models.CASCADE,
        related_name='user_select_departament',
        verbose_name=_('Отдел')
    )

    def __str__(self):
        return f'Отдел: {self.name}'

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = verbose_name + 'ы'


class EsUser(models.Model):
    unique_number = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_('Уникальный номер')
    )
    username = models.CharField(
        _('Ник'),
        max_length=30
    )
    password = models.CharField(
        _('Пароль'),
        max_length=10,
        unique=True
    )
    computer_info = models.FileField(
        _('Информация о компьютере'),
        upload_to='users/information/computer/',
        blank=True,
        null=True
    )
    ip_address = models.GenericIPAddressField(
        _('IP-адрес'),
        editable=False,
        blank=True,
        null=True
    )
    country_and_region = models.CharField(
        _('Страна и регион'),
        max_length=120,
        editable=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.password:
            self.password = generate_password()
        if not self.ip_address:
            self.ip_address = get_ip()
        if not self.country_and_region and self.ip_address:
            self.country_and_region = get_country_and_city(self.ip_address)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Пользователь: {self.username}'

    class Meta:
        verbose_name = 'Пользователь из тг'
        verbose_name_plural = 'Пользователи из тг'
