from django.contrib import admin
from .models import Table, Reservation, Order, Comment, UserProfile

admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(UserProfile)
