from base64 import encode
from pydoc import doc
import requests
import json
import os

from datetime import datetime

from decouple import config


class GetApi:
    def __init__(self, user):
        self._user = user
        self.main_dir = os.getcwd()
        # self.main_dir = os.path.join(os.getcwd(), 'utils')
        self.api_dir = os.path.join(self.main_dir, 'api')
        self.lang_dir = os.path.join(self.main_dir, 'lang')
        self.repos_dir = os.path.join(self.main_dir, 'repos')

    def get_api_repos(self):
        url = requests.get(
            f'https://api.github.com/users/{self._user}/repos'
        )
        response = url.text
        with open(os.path.join(self.api_dir, 'data.txt'), 'w') as file:
            for line in response:
                file.write(str(line))

    def get_api_commits(self):
        user = config('user')
        with open(os.path.join(self.api_dir, 'data.txt'), 'r') as file:
            data = file.read()
            repos = json.loads(data)
            for i in range(len(repos)):
                url = requests.get(f'https://api.github.com/repos/{user}/{repos[i]["name"]}/commits')
                response = url.json()
                with open(os.path.join(self.repos_dir, f"{repos[i]['name']}.txt"), 'w', encoding='utf-8') as file:
                    for line in response:
                        file.write(str(line))

    def get_api_languages(self):
        user = config('user')
        api_file = os.path.join(self.api_dir, 'data.txt')
        with open(api_file, 'r') as file:
            data = file.read()
            repos = json.loads(data)
            for i in range(len(repos)):
                url = requests.get(f'https://api.github.com/repos/{user}/{repos[i]["name"]}/languages')
                response = url.text
                with open(os.path.join(self.lang_dir, f"{repos[i]['name']}_lang.txt"), 'w', encoding='utf-8') as file:
                    for line in response:
                        file.write(str(line))
                
    def get_api_data(self):
        api = {}
        api_file = os.path.join(self.api_dir, 'data.txt')
        with open(api_file, 'r') as file:
            data = file.read()
            repos = json.loads(data)

            for i in range(len(repos)):
                with open(os.path.join(self.repos_dir, f'{repos[i]["name"]}.txt'), 'r') as file:
                    data = file.read()
                    commits = json.loads(data)

                with open(os.path.join(self.lang_dir, f'{repos[i]["name"]}_lang.txt'), 'r') as file:
                    data = file.read()
                    langs = json.loads(data)

                date = f"{commits[len(commits) - 1]['commit']['author']['date']}"
                hour = f"{commits[len(commits) - 1]['commit']['author']['date']}"

                created = f"{repos[i]['created_at']}"
                hour_created = f"{repos[i]['created_at']}"

                if repos[i]['archived'] == False:
                    repos[i]['archived'] = 'Ativo'
                else:
                    repos[i]['archived'] = 'Arquivado'
                
                api[i] = {
                    'name': repos[i]['name'],
                    'data': f'{created[0:10]} {hour_created[11:19]}',
                    'url': repos[i]['html_url'],
                    'status': repos[i]['archived'],
                    'commits': len(commits),
                    'last_commit': f'{date[0:10]} {hour[11:19]}',
                    'languagens' : [lang for lang in langs]

                }
        return api
            

if __name__ == '__main__':
    user = config('user')

    data = GetApi(user)
    data.get_api_repos()
    data.get_api_commits()
    data.get_api_languages()
    data.get_api_data()