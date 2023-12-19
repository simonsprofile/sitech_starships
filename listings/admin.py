from django.contrib import admin

from .models import Listing, Sale


admin.site.register(Listing)
admin.site.register(Sale)