import pandas as pd

df = pd.read_csv('repositories.csv')


average_stars_per_language = df.groupby('language')['stargazers_count'].mean().reset_index()

highest_average_language = average_stars_per_language.loc[average_stars_per_language['stargazers_count'].idxmax()]

print(f"Language with the highest average number of stars per repository: {highest_average_language['language']} with an average of {highest_average_language['stargazers_count']:.2f} stars.")
