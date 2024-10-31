import requests
import pandas as pd
import time
import os

from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('TOKEN')
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def get_user_repositories(username):
    repos_data = []
    url = f"https://api.github.com/users/{username}/repos"
    params = {
        "sort": "pushed", 
        "direction": "desc",
        "per_page": 100  
    }
    page = 1

    while len(repos_data) < 500:
        response = requests.get(url, headers=HEADERS, params={**params, "page": page})
        if response.status_code == 200:
            page_data = response.json()
            if not page_data:
                break 
            repos_data.extend(page_data)
            page += 1
        elif response.status_code == 403: 
            print("Rate limit reached. Pausing for a while...")
            time.sleep(60) 
        else:
            print(f"Failed to fetch repositories for {username}")
            break
    
   
    processed_repos = []
    for repo in repos_data[:500]: 
        processed_repos.append({
            "login": username,
            "full_name": repo["full_name"],
            "created_at": repo["created_at"],
            "stargazers_count": repo["stargazers_count"],
            "watchers_count": repo["watchers_count"],
            "language": repo["language"],
            "has_projects": repo["has_projects"],
            "has_wiki": repo["has_wiki"],
            "license_name": repo["license"]["key"] if repo["license"] else None
        })
    
    return processed_repos


def main():
    
    users_df = pd.read_csv('users.csv')
    all_repos_data = []

    
    for username in users_df['login']:
        print(f"Fetching repositories for user: {username}")
        user_repos = get_user_repositories(username)
        all_repos_data.extend(user_repos)
    
   
    repos_df = pd.DataFrame(all_repos_data)

   
    repos_df.to_csv('repositories.csv', index=False)


if __name__ == "__main__":
    main()
