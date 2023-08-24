from django.core.management.base import BaseCommand
from blogapp.models import Author, Post
from random import randint, choice


class Command(BaseCommand):
    help = "Generate fake posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        words = [
            'time', 'person', 'year', 'way', 'day', 'thing', 'man', 'World', 'life', 'hand',
            'part', 'child', 'eye', 'woman', 'place', 'week', 'case', 'point', 'government',
            'company', 'number', 'group', 'problem', 'fact', 'be', 'have', 'do', 'say', 'get',
            'make', 'go', 'know', 'take', 'see', 'come', 'think', 'look', 'want', 'give', 'use',
            'find', 'tell', 'ask', 'work', 'seem', 'feel', 'try', 'leave', 'call', 'good',
            'important', 'few', 'public', 'bad', 'same', 'able', 'any', 'first', 'to', 'of',
            'in', 'for', 'on', 'with', 'at', 'by', 'from', 'up', 'about', 'into', 'over',
            'after', 'the', 'and', 'a', 'that', 'I', 'it', 'not', 'he', 'as', 'you', 'this',
            'but', 'his', 'her', 'they', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would',
            'there', 'their', 'so', 'also', 'most'
        ]

        for author in Author.objects.all():
            for i in range(randint(1, count + 1)):
                count_words = randint(30, 100)
                post = Post(title=f'Post {i}',
                            content=choice(words).title() + ' ' +
                                    ' '.join(choice(words) for _ in range(count_words)),
                            author=author,
                            category=choice(['politics', 'economics', 'science', 'beauty',
                                             'news', 'thoughts', 'biology', 'chemistry',
                                             'history', 'physics', 'society']),
                            views=randint(0, 1000),
                            ispublic=choice([True, False]))
                post.save()
        self.stdout.write(f'fake posts created')
