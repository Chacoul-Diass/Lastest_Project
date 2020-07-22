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
			'fields':[
				'title',
				'telephone',
				'telephone2',
				'email',
				'email2',
				'address',
					]
		}),
	]


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Creto, CretoAdmin)