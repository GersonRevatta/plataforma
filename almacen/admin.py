from django.contrib import admin

# Register your models here.
from .models import Curso

from datetime import datetime, time, date, timedelta
admin.site.register(Curso)	



