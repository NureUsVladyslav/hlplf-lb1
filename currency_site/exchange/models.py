from django.db import models


class CurrencyRate(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Назва валюти")
    buy_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Курс купівлі")
    sell_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Курс продажу")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Курс валюти"
        verbose_name_plural = "Курси валют"
        ordering = ["name"]

    def __str__(self):
        return self.name


class DailyRateSnapshot(models.Model):
    currency = models.ForeignKey(CurrencyRate, on_delete=models.CASCADE, related_name="snapshots")
    snapshot_date = models.DateField(verbose_name="Дата")
    buy_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Курс купівлі")
    sell_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Курс продажу")
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Збережений курс"
        verbose_name_plural = "Збережені курси"
        unique_together = ("currency", "snapshot_date")
        ordering = ["currency__name"]

    def __str__(self):
        return f"{self.currency.name} - {self.snapshot_date}"