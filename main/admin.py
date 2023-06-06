from django.contrib import admin
from .models import Contributor, Repo

admin.site.register(Contributor)
admin.site.register(Repo)