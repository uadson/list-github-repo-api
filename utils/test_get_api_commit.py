import requests
import json
import os

def getApi():
    url = 'http://127.0.0.1:8000/api/repos/'
    response = requests.get(url)
    return response.json()

def getData():
    data = getApi()
    for i in data:
       api = i.values()
       print(api[i])


class GetApi:
    def __init__(self, user):
        self._user = user
        self.main_dir = os.getcwd()
        self.api_dir = os.path.join(self.main_dir, 'api')
        self.lang_dir = os.path.join(self.main_dir, 'lang')
        self.repos_dir = os.path.join(self.main_dir, 'repos')

    def get_api_repos(self):
        url = requests.get(
            f'https://api.github.com/users/{self._user}/repos'
        )
        try:
            response = url.text
            
            with open(os.path.join(self.api_dir, 'data.txt'), 'w') as file:
                for line in response:
                    file.write(str(line))

        except:
            return url.status_code

    def get_api_commits(self):
        user = 'uadson'
        with open(os.path.join(self.api_dir, 'data.txt'), 'r') as file:
            data = file.read()
            repos = json.loads(data)
            for i in range(len(repos)):
                url = requests.get(f'https://api.github.com/repos/{user}/{repos[i]["name"]}/commits')
                # response = url.text
                response = url.json()
              
                with open(os.path.join(self.repos_dir, f"{repos[i]['name']}.txt"), 'w', encoding='cp1252') as file:
                    for line in response:
                        file.write(str(line))


if __name__ == '__main__':

    data = GetApi('uadson')
    # data.get_api_repos()
    # data.get_api_commits()
    # data.get_api_languages()
    # data.get_api_data()

    getData()
