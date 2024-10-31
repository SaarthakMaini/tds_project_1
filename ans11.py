import pandas as pd


repositories_df = pd.read_csv("repositories.csv")

correlation = repositories_df['has_projects'].astype(int).corr(repositories_df['has_wiki'].astype(int))

print(f"{correlation:.3f}")
