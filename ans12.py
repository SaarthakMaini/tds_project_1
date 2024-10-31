import pandas as pd

users_df = pd.read_csv("users.csv")

users_df['hireable'] = users_df['hireable'].fillna('false').astype(bool)

hireable_users = users_df[users_df['hireable'] == 'true']
average_following_hireable = hireable_users['following'].mean() if len(hireable_users) > 0 else 0

non_hireable_users = users_df[users_df['hireable'] == False]
average_following_non_hireable = non_hireable_users['following'].mean() if len(non_hireable_users) > 0 else 0

difference = average_following_hireable - average_following_non_hireable

print(f"{difference:.3f}")
