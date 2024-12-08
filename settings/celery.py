import os
from celery import Celery

# Указываем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('settings')

# Чтение настроек из settings.py с префиксом CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматический поиск задач в файлах tasks.py
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
