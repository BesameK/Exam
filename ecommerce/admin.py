from django.contrib import admin

from ecommerce.models import *


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'start_time', 'end_time', 's_code')


class OrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "ticket")


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Order, OrderAdmin)
