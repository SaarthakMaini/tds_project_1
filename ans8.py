import pandas as pd

df = pd.read_csv('users.csv')


df['leader_strength'] = df['followers'] / (1 + df['following'])

top_leader_strength = df.sort_values(by='leader_strength', ascending=False).head(5)


top_user_logins = ', '.join(top_leader_strength['login'].tolist())

print("Top 5 users in terms of leader strength:", top_user_logins)
