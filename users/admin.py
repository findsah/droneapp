from django.contrib import admin
from .models import customer, seller, controlroom


# Register your models here.

@admin.register(customer)
class custom_userAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'email_address']

    class Meta:
        model = customer


@admin.register(seller)
class info_userAdmin(admin.ModelAdmin):
    list_display = [ 'id','location', 'email_address','phone']

    class Meta:
        model = seller


@admin.register(controlroom)
class adminnrAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'location']

    class Meta:
        model = controlroom