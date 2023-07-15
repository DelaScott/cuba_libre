from django.contrib import admin
from .models import Property, Booking, Email, Phone


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'price', 'available']
    list_filter = ['available']
    search_fields = ['title', 'description']
    filter_horizontal = ['emails', 'phone']

    fieldsets = (
        (None, {
            'fields': ('title', 'owner', 'price', 'available')
        }),
        ('Description', {
            'fields': ('description', 'image')
        }),
        ('Room and Guest Information', {
            'fields': ('num_rooms', 'num_guests')
        }),
        ('Contact Information', {
            'fields': ('phone', 'emails')
        })
    )
admin.site.register(Booking)
admin.site.register(Email)
admin.site.register(Phone)
