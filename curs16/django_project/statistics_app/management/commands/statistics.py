from django.core.management.base import BaseCommand, CommandError
from job_list.models import Post
from datetime import date


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(Post.objects.filter(date_expire__gte=date.today()))