from import_export import resources
from .models import ScrapperData


class ScrapedDataResource(resources.ModelResource):
    class Meta:
        model = ScrapperData
