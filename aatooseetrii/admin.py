from django.contrib import admin

from .models import CatTable, GreatWordsTable, NatPark, Seuraaja

admin.site.register(CatTable)
admin.site.register(GreatWordsTable)
admin.site.register(NatPark)
admin.site.register(Seuraaja)
