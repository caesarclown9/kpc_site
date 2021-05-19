from import_export import resources
from .models import Tables


class TablesResources(resources.ModelResource):
    class Meta:
        model = Tables
        fields = ['num','params', 'norms', 'method', 'note']
        # exclude = ('name', 'id')
        import_id_fields = ['num']
