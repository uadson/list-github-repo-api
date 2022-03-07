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

	def get_repo_commits(self):
		repo_data = self.get_repo()
		commits = {}
		for i in range(len(repo_data)):
			response = requests.get(
				f'https://api.github.com/repos/{USER}/{repo_data[i]["name"]}/commits',
				auth=(USER, TOKEN)
			)
			commits[i]=response.json()
		return commits

	def get_repo_lang(self):
		repo_data = self.get_repo()
		for i in range(len(repo_data)):
			response = requests.get(
				f'https://api.github.com/repos/{USER}/{repo_data[i]["name"]}/languages',
				auth=(USER, TOKEN)
			)
			if response.status_code == 200:
				return response.json()
			else:
				return response.status_code

	def get_repo_api(self):
		try:
			repo_data = self.get_repo()
			repo_commits = self.get_repo_commits()
			print(repo_commits[0][0]['commit']['author']['date'])
			repo_langs = self.get_repo_lang()

			api_data = {}

			for i in range(len(repo_data)):

				date = f"{repo_commits[len(repo_commits[i]) - 1][0]['commit']['author']['date']}"
				hour = f"{repo_commits[len(repo_commits[i]) - 1][0]['commit']['author']['date']}"

				created = f"{repo_data[i]['created_at']}"
				hour_created = f"{repo_data[i]['created_at']}"

				if repo_data[i]['archived'] == False:
					repo_data[i]['archived'] = 'Ativo'
				else:
					repo_data[i]['archived'] = 'Arquivado' 

				api_data[i] = {
					'name': repo_data[i]['name'],
					'url': repo_data[i]['html_url'],
					'date': f'{created[0:10]} {hour_created[11:19]}',
					'status': repo_data[i]['archived'],
					'commits': len(repo_commits),
					'last_commit': f'{date[0:10]} {hour[11:19]}',
					'languages': repo_langs
				}
				return api_data

		except KeyError:
			return 'Error'
	
	def save(self, *args, **kwargs):
		self.data = self.get_repo_api()
		super().save(*args, **kwargs)
