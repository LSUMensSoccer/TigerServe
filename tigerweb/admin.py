from django.contrib import admin

# Register your models here.
from tigerweb.models import Officer, Player

admin.site.register(Officer)
admin.site.register(Player)