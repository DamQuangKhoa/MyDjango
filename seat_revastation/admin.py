from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['code','is_disable']
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass