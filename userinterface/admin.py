from django.contrib import admin
from .models import News  # ✅ Make sure this matches your model

admin.site.register(News)
