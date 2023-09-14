from faker import Faker
import faktory
from faker.providers import internet
from django.conf import settings
from apps.blog.models import Post

locale = [settings.LANGUAGE_CODE, 'en_US']

faker = Faker()
faker.add_provider(internet)

def generate_posts(count):
    for _ in count:
        post = Post.objects.create(
            title=faker.unique().name(),
            description = faker.text(250),
            thumbnail=faker.image_url(),
            
        )
        post.save()
        

class PostFactory(factory.Factory):
    class Meta:
        model = Post
    
    title = factory.Faker('sentence', nb_words=4)
    