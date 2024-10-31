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

def clean_company(company):
    if pd.isna(company):
        return ''
    company = company.strip()       
    if company.startswith('@'):    
        company = company[1:]
    return company.upper()         

def get_hyderabad_users():
    print("Getting hyderabad users")
    users_data = []
    url = "https://api.github.com/search/users"
    params = {"q": "location:Hyderabad followers:>50"}

    response = requests.get(url, headers=HEADERS, params=params)
    response_data = response.json()

    for user in response_data.get("items", []):
        user_details = get_user_details(user["login"])
        if user_details:
            users_data.append(user_details)
    
    return users_data

def get_user_details(username):
    print("getting user details...")
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        user_data = response.json()
        return {
            "login": user_data["login"],
            "name": user_data["name"],
            "company": clean_company(user_data["company"]),
            "location": user_data["location"],
            "email": user_data["email"],
            "hireable": user_data["hireable"],
            "bio": user_data["bio"],
            "public_repos": user_data["public_repos"],
            "followers": user_data["followers"],
            "following": user_data["following"],
            "created_at": user_data["created_at"]
        }
    elif response.status_code == 403: 
        print("Rate limit reached. Pausing for a while...")
        time.sleep(60)  
        return get_user_details(username)
    else:
        print(f"Failed to fetch data for {username}")
        return None


def main():
    users_data = get_hyderabad_users()

    
    df = pd.DataFrame(users_data)

   
    df.to_csv('users.csv', index=False)


if __name__ == "__main__":
    main()