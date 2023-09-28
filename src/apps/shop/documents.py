from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Product


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
        
    # name = fields.TextField(attr="name", fields={
    #                         "suggest": fields.Completion()})

    class Django:
        model = Product
        fields = ["id", 'title']
