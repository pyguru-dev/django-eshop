from faker import Faker

from apps.blog.models import Post

faker = Faker()

def generate_posts(count):
    for _ in count:
        post = Post.objects.create(
            title=faker.name(),
            description = faker.text(250),
            thumbnail=faker.image_url(),
            
        )
        post.save()