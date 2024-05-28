import requests


def fetch_user_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        repos_list = []
        for repo in repos:
            repo_dict = {}
            for key in repo:
                if key == 'name' or key == 'description' or key == 'language' or key == 'stargazers_count':
                    repo_dict[key] = repo[key]
            repos_list.append(repo_dict)
    return repos_list


def display_repository_info(repositories):
    for repo in repositories:
        print(f"Name: {repo['name']}")
        print(f"Description: {repo['description']}")
        print(f"Language: {repo['language']}")
        print(f"Stars: {repo['stargazers_count']}")


def main():
    username = input("Enter a GitHub username: ")
    repos = fetch_user_repositories(username)
    display_repository_info(repos)


main()
