from faker import Faker

faker = Faker()

def generate_posts(count):
    for _ in count:
        post = Post.objects.create(
            title=faker.title()
        )
        post.save()