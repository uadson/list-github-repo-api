import requests
import json
from datetime import datetime


class Repos():
	def __init__(self, usuario):
		self._usuario = usuario

	def requisicao_api(self):
		resposta = requests.get(
			f'https://api.github.com/users/{self._usuario}/repos')
		if resposta.status_code == 200:
			return resposta.json()
		else:
			return resposta.status_code

	def imprime_repositorios(self):
		dados_api = self.requisicao_api()
		if type(dados_api) is not int:
			for i in range(len(dados_api)):
				# nome
				print(dados_api[i]['name'])

				# data do último commmit
				valores = dados_api[i]['pushed_at']
				dia = valores[8:10]
				mes = valores[5:7]
				ano = valores[0:4]
				formato = datetime(int(ano), int(mes), int(dia)) 
				data = formato.strftime('%d/%m/%Y')
				print(data)

				# se está arquivado
				if dados_api[i]['archived'] == True:
					print('Arquivado')
				else:
					print('Ativo')

				# linguagem
				if dados_api[i]['language'] == None:
					print('Sem linguagem definida')
				else:
					print(dados_api[i]['language'])
		else:
			print(dados_api)

	def requisicao_commit(self):
		resposta = requests.get(
			f'https://api.github.com/repos/uadson/studies/commits')
		if resposta.status_code == 200:
			return resposta.json()
		else:
			return resposta.status_code

	def imprime_commits(self):
		dados_commit = self.requisicao_commit()
		print(f'Quantidade de commits = {len(dados_commit)}')
		print(f'Data do último commit: {dados_commit[len(dados_commit) - 1]["commit"]["author"]["date"]}')
		if type(dados_commit) is not int:
			for i in range(len(dados_commit)):
				print(dados_commit[i]['commit']['author']['date'])

	def requisicao_languages(self):
		resposta = requests.get(
			f'https://api.github.com/repos/uadson/studies/languages')
		if resposta.status_code == 200:
			return resposta.json()
		else:
			return resposta.status_code

	def imprime_languages(self):
		dados_languages = self.requisicao_languages()
		for i in dados_languages.keys():
			print(i)


if __name__ == '__main__':
	repos = Repos('uadson')
	repos.imprime_repositorios()
	repos.imprime_commits()
	repos.imprime_languages()