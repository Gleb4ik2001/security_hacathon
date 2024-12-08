from django.contrib import admin
from .models import (
    Vulnerability,
    ScanResult
)

admin.site.register(Vulnerability)
admin.site.register(ScanResult)
