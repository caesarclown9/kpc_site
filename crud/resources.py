from import_export import resources
from .models import Tables


class TablesResources(resources.ModelResource):
    class Meta:
        model = Tables
        # fields = [field.name for field in Tables._meta.fields]
        exclude = ['name']
        # import_id_fields = ['num']
