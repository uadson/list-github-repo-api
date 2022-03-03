from django.db import models

from decouple import config

from utils.get_api_data import GetApi


class Repository(models.Model):
	user = models.CharField(max_length=20)
	data = models.JSONField(blank=True)

	class Meta:
		verbose_name = 'respository'
		verbose_name_plural = 'repositories'
		db_table = 'repositories'

	def save(self, *args, **kwargs):
		if self.data is None:
			data = GetApi(self.user)
			self.data = data.get_api_data()
		super().save(*args, **kwargs)
