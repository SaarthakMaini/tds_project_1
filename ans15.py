import pandas as pd

users_df = pd.read_csv("users.csv")


users_df['hireable'] = users_df['hireable'].fillna(False).astype(bool)


hireable_users = users_df[users_df['hireable'] == True]
hireable_with_email = hireable_users['email'].notna().sum()
fraction_hireable_with_email = hireable_with_email / len(hireable_users) if len(hireable_users) > 0 else 0


non_hireable_users = users_df[users_df['hireable'] == False]
non_hireable_with_email = non_hireable_users['email'].notna().sum()
fraction_non_hireable_with_email = non_hireable_with_email / len(non_hireable_users) if len(non_hireable_users) > 0 else 0


difference = fraction_hireable_with_email - fraction_non_hireable_with_email


print(f"{difference:.3f}")
