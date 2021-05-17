from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *
from .resources import TablesResources


class RatesAdmin(admin.ModelAdmin):
    model = Rates
    list_display = ['form', 'tax', 'ai_80', 'diesel1', 'diesel2', 'fuel_oil']
    list_editable = ['form', 'tax', 'ai_80', 'diesel1', 'diesel2', 'fuel_oil']

@admin.register(Tables)
class TablesAdmin(ImportExportModelAdmin):
    resource_class = TablesResources
    list_display = ('params', 'norms', 'method', 'note')

admin.site.register(News)
admin.site.register(Rates)
admin.site.register(Leaders)
admin.site.register(Slides)


