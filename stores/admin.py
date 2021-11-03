from django.contrib import admin
from stores.models import Stores,Products,Orders,drones


@admin.register(Stores)
class CourseAdmin(admin.ModelAdmin):
    list_display = [ 'name']

    class Meta:
        model = Stores


@admin.register(Products)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Products


@admin.register(Orders)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['ordernumber']

    class Meta:
        model = Orders

@admin.register(drones)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = drones