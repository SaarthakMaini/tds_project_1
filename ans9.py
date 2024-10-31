import pandas as pd


users_df = pd.read_csv("users.csv")


correlation = users_df['followers'].corr(users_df['public_repos'])


print(f"{correlation:.3f}")
