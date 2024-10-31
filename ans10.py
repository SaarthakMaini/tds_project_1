import pandas as pd
from scipy.stats import linregress


users_df = pd.read_csv("users.csv")


slope, intercept, r_value, p_value, std_err = linregress(users_df['public_repos'], users_df['followers'])


print(f"{slope:.3f}")
