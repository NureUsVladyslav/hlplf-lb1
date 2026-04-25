from datetime import date
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import CurrencyRate, DailyRateSnapshot


def rate_list(request):
    rates = CurrencyRate.objects.all()
    return render(request, "exchange/rate_list.html", {"rates": rates})


def save_today_rates(request):
    if request.method == "POST":
        today = date.today()
        rates = CurrencyRate.objects.all()

        for rate in rates:
            DailyRateSnapshot.objects.update_or_create(
                currency=rate,
                snapshot_date=today,
                defaults={
                    "buy_rate": rate.buy_rate,
                    "sell_rate": rate.sell_rate,
                },
            )

    return redirect("today_rates")


def today_rates(request):
    today = date.today()
    snapshots = DailyRateSnapshot.objects.filter(snapshot_date=today).select_related("currency")
    return render(
        request,
        "exchange/today_rates.html",
        {
            "snapshots": snapshots,
            "today": today,
        },
    )


def today_rates_api(request):
    today = date.today()
    rates = CurrencyRate.objects.all()

    data = [
        {
            "name": rate.name,
            "buy_rate": str(rate.buy_rate),
            "sell_rate": str(rate.sell_rate),
            "date": str(today),
        }
        for rate in rates
    ]

    return JsonResponse(
        {
            "date": str(today),
            "rates": data,
        }
    )

