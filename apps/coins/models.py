from django.conf import settings
from django.db import models

class CoinBalance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователи", related_name="user_coin")
    balance = models.CharField(max_length=255, blank=True, default=4, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.balance} Geek Coins"
    
    class Meta:
        verbose_name = "Просмотр баланса"
        verbose_name_plural = "Просмотр баланса"
