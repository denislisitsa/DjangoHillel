from django.core.management.base import BaseCommand
from models import Teacher
import random


class Command(BaseCommand):
    help = 'Генерирует случайных учителей'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=100, help='Number of teachers to generate')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        teachers = [
            Teacher(
                name=f'Teacher {i+1}',
                age=random.randint(25, 65),
                subject=f'Subject {random.randint(1, 5)}',
                years_of_experience=random.randint(1, 40)
            ) for i in range(count)
        ]
        Teacher.objects.bulk_create(teachers)
        self.stdout.write(self.style.SUCCESS(f'Удачно создано {count} учителей'))
