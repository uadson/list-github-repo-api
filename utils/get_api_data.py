import requests
import json

from datetime import datetime

from decouple import config


class GetApi:
    def __init__(self, user):
        self._user = user

    def get_api_repos(self):
        url = requests.get(
            f'https://api.github.com/users/{self._user}/repos'
        )
        if url.status_code == 200:
            response = url.text
            
            with open('api/data.txt', 'w') as file:
                for line in response:
                    file.write(str(line))
       
        else:
            return url.status_code

    def get_api_commits(self):
        user = config('user')
        with open('api/data.txt', 'r') as file:
            data = file.read()
            repos = json.loads(data)
            for i in range(len(repos)):
                
                url = requests.get(
                    f'https://api.github.com/repos/{user}/{repos[i]["name"]}/commits'
                )
                if url.status_code == 200:
                    response = url.text
                
                    with open(f"repos/{repos[i]['name']}.txt", 'w') as file:
                        for line in response:
                            file.write(str(line))
                else:
                    return url.status_code

    def get_api_languages(self):
        user = config('user')
        with open('api/data.txt', 'r') as file:
            data = file.read()
            repos = json.loads(data)

            for i in range(len(repos)):
                url = requests.get(
                    f'https://api.github.com/repos/{user}/{repos[i]["name"]}/languages'
                )
                if url.status_code == 200:
                    response = url.text

                    with open(f"lang/{repos[i]['name']}_lang.txt", 'w') as file:
                        for line in response:
                            file.write(str(line))
                
                else:
                    return url.status_code

    def get_api_data(self):
        api = {}

        with open('api/data.txt', 'r') as file:
            data = file.read()
            repos = json.loads(data)

            for i in range(len(repos)):
                with open(f'repos/{repos[i]["name"]}.txt', 'r') as file:
                    data = file.read()
                    commits = json.loads(data)

                with open(f'lang/{repos[i]["name"]}_lang.txt', 'r') as file:
                    data = file.read()
                    langs = json.loads(data)

                date = f"{commits[len(commits) - 1]['commit']['author']['date']}"
                hour = f"{commits[len(commits) - 1]['commit']['author']['date']}"
                
                api[i] = {
                    'name': repos[i]['name'],
                    'url': repos[i]['html_url'],
                    'status': repos[i]['archived'],
                    'commits': len(commits),
                    'last_commit': datetime.strptime(f'{date[0:10]} {hour[11:19]}', '%d/%m/%Y %H:%M:%S'),
                    'languagens' : [lang for lang in langs]

                }
        return api
            

if __name__ == '__main__':
    user = config('user')

    data = GetApi(user)
    # data.get_api_repos()
    # data.get_api_commits()
    # data.get_api_languages()
    data.get_api_data()