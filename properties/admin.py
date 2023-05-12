from django.contrib import admin
from .models import House, Building, Apartment, Payment, Media

# Register your models here.
admin.site.register(House)
admin.site.register(Building)
admin.site.register(Apartment)
admin.site.register(Payment)
admin.site.register(Media)
