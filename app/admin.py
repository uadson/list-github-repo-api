from django.contrib import admin

from app.models import Repository


@admin.register(Repository)
class RepoAdmin(admin.ModelAdmin):
	pass
