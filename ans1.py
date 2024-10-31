import pandas as pd

df = pd.read_csv('users.csv')

top_users = df.sort_values(by='followers', ascending=False).head(5)

top_user_logins = ', '.join(top_users['login'].tolist())

print("Top 5 users in Hyderabad with the highest number of followers:", top_user_logins)
