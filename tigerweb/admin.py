from django.contrib import admin

# Register your models here.
from tigerweb.models import Officer, Player, Event

admin.site.register(Officer)
admin.site.register(Player)
admin.site.register(Event)