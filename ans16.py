import pandas as pd
from collections import Counter

users_df = pd.read_csv('users.csv')


surnames = []


for name in users_df['name']:
    if pd.notna(name): 
        surname = name.strip().split()[-1]  
        surnames.append(surname)


surname_counts = Counter(surnames)


max_count = max(surname_counts.values())

most_common_surnames = [surname for surname, count in surname_counts.items() if count == max_count]

most_common_surnames.sort()


result = ', '.join(most_common_surnames)
print("Most common surname(s):", result)
