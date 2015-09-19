from django.contrib import admin

from events.models import Event, EventPart

admin.site.register(Event)

admin.site.register(EventPart)
