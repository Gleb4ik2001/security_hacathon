from celery import shared_task
from .parser import run_parser  # Импорт функции вашего парсера

@shared_task
def scheduled_parser():
    print("Запуск парсера...")
    run_parser()
    print("Парсер завершён.")
