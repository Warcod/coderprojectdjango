from django.contrib import admin
from .models import Movies, Series, Songs

admin.site.register(Movies)
admin.site.register(Songs)
admin.site.register(Series)


# Register your models here.
