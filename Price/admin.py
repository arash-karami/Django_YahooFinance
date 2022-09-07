from django.contrib import admin
from .models import Ticker , Data



admin.register(Ticker, Data)(admin.ModelAdmin)