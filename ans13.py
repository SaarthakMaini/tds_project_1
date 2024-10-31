import pandas as pd
import statsmodels.api as sm

users_df = pd.read_csv('users.csv')


users_df['bio_word_count'] = users_df['bio'].apply(lambda x: len(str(x).split()) if pd.notna(x) else 0)

filtered_df = users_df[users_df['bio_word_count'] > 0]

X = filtered_df['bio_word_count']
y = filtered_df['followers']

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

slope = model.params['bio_word_count']

print(f"Regression slope of followers on bio word count: {slope:.3f}")
