from django.contrib import admin
from .models import (
    PyContent,
    ProgContent,
    HiringContent,
    CovidContent,
)
# Register your models here.
admin.site.register(PyContent)
admin.site.register(ProgContent)
admin.site.register(HiringContent)
admin.site.register(CovidContent)