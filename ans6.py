import pandas as pd

df = pd.read_csv('repositories.csv')

df['created_at'] = pd.to_datetime(df['created_at'])

new_users = df[df['created_at'] >= '2020-01-01']

languages_series = new_users['language'].dropna().str.split(', ').explode()

popular_languages = languages_series.value_counts()

second_most_popular_language = popular_languages.index[1] if len(popular_languages) > 1 else "Not enough languages found"

print("Second most popular programming language among users who joined after 2020:", second_most_popular_language)
