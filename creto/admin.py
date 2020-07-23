from django.contrib import admin
from creto import models


# Register your models here.


class CretoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'telephone',
        'telephone2',
        'email',
        'email2',
        'address',
        'date_cre',
        'date_mod',
    )

    fieldsets = [
        ('Info', {
            'fields': [
                'title',
                'telephone',
                'telephone2',
                'email',
                'email2',
                'address',
            ]
        }),
    ]


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'phone',
        'email',
        'message',
        'date_add',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'nom',
    )
    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields': [
                'nom',
                'phone',
                'email',
                'message',
            ]
        }),
    ]


class SuscribeAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'date_add',
        'date_update',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'email',
    )
    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields': [
                'email',
            ]
        }),
    ]

class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'titre',

    )
    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields': [
                'titre',
                'photo',
            ]
        }),
    ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Creto, CretoAdmin)
_register(models.Contact, ContactAdmin)
_register(models.Suscribe, SuscribeAdmin)
_register(models.PhotoGallery, PhotoGalleryAdmin)
