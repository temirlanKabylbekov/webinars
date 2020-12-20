import requests


def get_github_user_info(username):
    try:
        return requests.get(f'https://api.github.com/users/{username}')
    except requests.exceptions.Timeout:
        return {}


def get_full_user_info(username):
    github_info = get_github_user_info(username)
    if github_info:
        return f'{github_info["name"]} | followers: {github_info["followers"]} | following: {github_info["following"]}'
