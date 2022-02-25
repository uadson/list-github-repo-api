import requests
import json

from datetime import datetime

from django.db import models

from core.models import User


class Base(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		abstract = True


class Repository(Base):
	user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
	name = models.CharField('Name:', max_length=200)
	url = models.URLField('URL:', max_length=200)
	date = models.DateField('Data de Criação:')
	commits = models.IntegerField('Commits:')
	languages = models.CharField('Linguagens:', max_length=200)
	last_commit = models.DateField('Data do último commit:')
	status = models.CharField('Status:', max_length=100)

	class Meta:
		verbose_name = 'repository'
		verbose_name_plural = 'repositories'
		ordering = ['-name']
