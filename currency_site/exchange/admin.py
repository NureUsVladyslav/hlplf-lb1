from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import CurrencyRate


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ("name", "buy_rate", "sell_rate")
    fields = ("name", "buy_rate", "sell_rate")
    search_fields = ("name",)