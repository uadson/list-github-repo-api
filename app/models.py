import requests
import json

from django.db import models

from decouple import config

from utils.get_api_data import GetApi

from backend.settings.base import USER, TOKEN


class Repository(models.Model):
	data = models.JSONField(blank=True)

	class Meta:
		verbose_name = 'respository'
		verbose_name_plural = 'repositories'
		db_table = 'repositories'

	def get_repo(self):
		response = requests.get(
			f'https://api.github.com/users/{USER}/repos',
			auth=(USER, TOKEN)
		)
		if response.status_code == 200:
			return response.json()
		else:
			return response.status_code

	def get_repo_lang(self):
		repo_data = self.get_repo()
		data = {}
		langs = {}

		for i in range(len(repo_data)):
			response = requests.get(
				f'https://api.github.com/repos/{USER}/{repo_data[i]["name"]}/languages',
				auth=(USER, TOKEN)
			)
			data[i] = response.json()

		for i in range(len(data.items())):
			if len(data.get(i).keys()) > 1:
				langs[i] = [lang for lang in data.get(i).keys()]
				langs[i] = ', '.join(langs[i])
			elif len(data.get(i).keys()) == 1:
				langs[i] = [lang for lang in data.get(i).keys()]
				langs[i] = ''.join(langs[i])
			else:
				langs[i] = '-'

		return langs

	def get_repo_api(self):
		try:
			repo_data = self.get_repo()
			repo_langs = self.get_repo_lang()

			api_data = {}

			for i in range(len(repo_data)):

				created = f"{repo_data[i]['created_at']}"
				hour_created = f"{repo_data[i]['created_at']}"

				updated = f"{repo_data[i]['updated_at']}"
				hour_updated = f"{repo_data[i]['updated_at']}"

				if repo_data[i]['fork'] == True:
					repo_data[i]['fork'] = 'Sim'
				else:
					repo_data[i]['fork'] = 'Não'

				if repo_data[i]['archived'] == False:
					repo_data[i]['archived'] = 'Ativo'
				else:
					repo_data[i]['archived'] = 'Arquivado'


				api_data[i] = {
					'name': repo_data[i]['name'],
					'url': repo_data[i]['html_url'],
					'date': f'{created[0:10]} {hour_created[11:19]}',
					'fork': repo_data[i]['fork'],
					'status': repo_data[i]['archived'],
					'updated': f'{updated[0:10]} {hour_updated[11:19]}',
					'languages': repo_langs.get(i)
				}

			
			return api_data

		except Exception as error:
			return error
	
	def save(self, *args, **kwargs):
		self.data = self.get_repo_api()
		super().save(*args, **kwargs)
