from django.db import models

class Exploit(models.Model):
    vuln_id = models.CharField(max_length=255, unique=True)  # ID уязвимости
    title = models.CharField(max_length=500)  # Название уязвимости
    date = models.DateField()  # Дата публикации
    source_url = models.URLField()  # Ссылка на источник
    exploit_links = models.TextField()  # Ссылки на PoC/эксплойты

    def __str__(self):
        return self.title

