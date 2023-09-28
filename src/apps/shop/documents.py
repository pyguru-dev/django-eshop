from django_elasticsearch_dsl import Document, Index, fields

from .models import Product

product_index = Index("products")
product_index.settings(
    number_of_shards=1,
    number_of_replicas=0,
)


@product_index.doc_type
class ProductDocument(Document):
    name = fields.TextField(attr="name", fields={
                            "suggest": fields.Completion()})

    class Django:
        model = Product
        fields = ["id", 'title', "price"]
