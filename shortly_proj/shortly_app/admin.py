from django.contrib import admin

# Register your models here.

from shortly_app.models import Shortly, ShortlyInfo  # Snippet

# admin.site.register(Snippet)
admin.site.register(Shortly)
admin.site.register(ShortlyInfo)
