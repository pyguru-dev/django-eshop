from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Post

# ./manage.py search_index --rebuild


@registry.register_document
class PostDocument(Document):
    class Index:
        name = 'posts'

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Post

        fields = [
            'title',
            'description',
        ]


        # ignore_signals = True

        # auto_refresh = False

        # queryset_pagination = 5000
