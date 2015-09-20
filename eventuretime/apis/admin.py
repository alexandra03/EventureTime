from django.contrib import admin

from apis.models import Instagram, Yelp, Uber

# Register your models here.

admin.site.register(Instagram)
admin.site.register(Yelp)
admin.site.register(Uber)
