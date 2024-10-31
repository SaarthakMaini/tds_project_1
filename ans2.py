import pandas as pd

users_df = pd.read_csv('users.csv')

hyderabad_users = users_df[users_df['location'].str.contains('Hyderabad', na=False)]
hyderabad_users['created_at'] = pd.to_datetime(hyderabad_users['created_at'])

earliest_users = hyderabad_users.nsmallest(5, 'created_at')

earliest_logins = earliest_users['login'].tolist()
earliest_logins_result = ', '.join(earliest_logins)

print(f"The 5 earliest registered users in Hyderabad are: {earliest_logins_result}")
