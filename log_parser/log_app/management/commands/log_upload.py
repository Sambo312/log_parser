import time
from logging import getLogger

from django.core.management.base import BaseCommand

from log_app.utils import LogUploader


logger = getLogger(__name__)


class Command(BaseCommand):
    help = 'Загрузка логов из файла'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            help='Необходимо указать полный путь к файлу'
        )

    def handle(self, *args, **options):
        start = time.time()
        logger.info(f'Загрузка логов из файла')
        self.proccess(*args, **options)
        logger.info(f'Общее время выполнения: {time.time() - start}')

    def proccess(self, *args, **options):
        LogUploader().handle(options=options)
