from faker import Faker
from faker.providers import lorem
from blogapp.models import Post
from django.contrib.auth.models import User

user = User.objects.get(username="admin")
fake = Faker()
fake.add_provider(lorem)

for _ in range(100):
    title: str = fake.sentence(nb_words=6)
    slug: str = "-".join(title.lower().split())
    body: str = fake.paragraph(nb_sentences=15)
    Post.objects.create(title=title, slug=slug, body = body, author = user)
