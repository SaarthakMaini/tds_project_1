import pandas as pd

users_df = pd.read_csv('users.csv')

users_df['company'] = users_df['company'].str.strip().str.upper()

company_counts = users_df['company'].value_counts()

most_common_company = company_counts.idxmax()
most_common_count = company_counts.max()

result = f"The majority of developers work at: {most_common_company} with {most_common_count} developers."
print(result)
