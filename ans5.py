import pandas as pd


df = pd.read_csv('repositories.csv')


languages_series = df['language'].dropna().str.split(', ').explode()


popular_languages = languages_series.value_counts().head(1)

most_popular_language = popular_languages.index[0] if not popular_languages.empty else "No languages found"

print("Most popular programming language among users in Hyderabad:", most_popular_language)
