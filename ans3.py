import pandas as pd

repos_df = pd.read_csv('repositories.csv')

licenses = repos_df['license_name'].dropna()

top_licenses = licenses.value_counts().head(3).index.tolist()

top_licenses_result = ', '.join(top_licenses)
print(f"The 3 most popular licenses are: {top_licenses_result}")
