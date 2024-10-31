import pandas as pd


repositories_df = pd.read_csv("repositories.csv")


repositories_df['created_at'] = pd.to_datetime(repositories_df['created_at'])


weekend_repos = repositories_df[repositories_df['created_at'].dt.dayofweek.isin([5, 6])]


top_users = weekend_repos.groupby('login').size().reset_index(name='repo_count')


top_users = top_users.sort_values(by='repo_count', ascending=False)


top_5_users = top_users.head(5)


top_5_logins = ', '.join(top_5_users['login'].astype(str))
print(top_5_logins)
