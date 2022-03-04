import requests
import json

from django.db import models

from decouple import config

from utils.get_api_data import GetApi


from django.shortcuts import Http404


class Repository(models.Model):
	user = models.CharField(max_length=20)
	data = models.JSONField(blank=True)

	class Meta:
		verbose_name = 'respository'
		verbose_name_plural = 'repositories'
		db_table = 'repositories'

	def get_repo(self):
		repo_url = requests.get(
			f'https://api.github.com/users/{self.user}/repos'
		)
		if repo_url.status_code == 200:
			return repo_url.json()
		else:
			return repo_url.status_code

	def get_repo_commits(self):
		repo_data = self.get_repo()
		commits = {}
		if type(repo_data) is not int:
			for i in range(len(repo_data)):
				repo_commits = requests.get(
					f'https://api.github.com/repos/{self.user}/{repo_data[i]["name"]}/commits'
				)
				if repo_commits.status_code == 200:
					for j in repo_commits:
						commits[j]= j
					return commits
				else:
					repo_commits.status_code

	def get_repo_lang(self):
		repo_data = self.get_repo()
		langs = []
		if type(repo_data) is not int:
			for i in range(len(repo_data)):
				repo_langs = requests.get(
					f'https://api.github.com/repos/{self.user}/{repo_data[i]["name"]}/languages'
				)
				if repo_langs.status_code == 200:
					
					return repo_langs.json()
				else:
					return repo_langs.status_code

	def get_repo_api(self):
		try:
			repo_data = self.get_repo()
			repo_commits = self.get_repo_commits()
			repo_langs = self.get_repo_lang()

			print(len(repo_commits))
			api_data = {}
			if type(repo_data) and type(repo_commits) and type(repo_langs) is not int:

				for i in range(len(repo_data)):

					# date = f"{repo_commits[len(repo_commits) - 1]['commit']['author']['date']}"
					# hour = f"{repo_commits[len(repo_commits) - 1]['commit']['author']['date']}"

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
						# 'last_commit': f'{date[0:10]} {hour[11:19]}',
						'languages': repo_langs
					}
				return api_data

		except KeyError:
			return Http404()
	
	def save(self, *args, **kwargs):
		self.data = self.get_repo_api()
		super().save(*args, **kwargs)
