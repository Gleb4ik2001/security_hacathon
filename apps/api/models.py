from django.db import models


class Vulnerability(models.Model):
    vul_id = models.CharField(
        verbose_name='айди уязвимости',
        max_length=100,
        unique=True
    )
    title = models.CharField(
        verbose_name='название',
        max_length=255
    )
    description = models.TextField(
        verbose_name='описание'
    )
    published_date = models.DateTimeField(
        'дата публикации'
    )
    source_url = models.URLField(
        verbose_name='исходная ссылка'
    )
    exploit_data = models.TextField(
        verbose_name='эксплойты и PoC',
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='уязвимость'
        verbose_name_plural = 'уязвимости'
        ordering = ('-id',)


class ScanResult(models.Model):
    ip_or_domain = models.CharField(
        verbose_name='айпи/домен',
        max_length=255
    )
    status = models.CharField(
        max_length=50, 
        choices=[
            ('vulnerable', 'Vulnerable'),
            ('not_vulnerable', 'Not Vulnerable'),
            ('error', 'Error'),
        ]
    )
    applied_exploits = models.TextField(
        verbose_name='прикладные эксплойты'
    )
    services_found = models.TextField(
        verbose_name='найденные сервисы',
        blank=True, 
        null=True
    )
    scan_date = models.DateTimeField(
        verbose_name='дата сканирования',
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.ip_or_domain} - {self.status}"
    
    class Meta:
        verbose_name = 'рузльтат сканирования'
        verbose_name_plural = 'результаты сканирования'
        ordering = ('-id',)