import pandas as pd

# Load raw leads
df = pd.read_csv('raw_leads.csv')

# Basic cleaning for Home Loan leads
df.drop_duplicates(subset=['phone'], inplace=True)
df['city'] = df['city'].str.lower().str.strip()
df['loan_amount'] = df['loan_amount'].fillna(df['loan_amount'].median())

# Lead Quality Score logic
df['quality_score'] = df.apply(lambda x: 10 if x['salary'] > 50000 and x['cibil'] > 700 else 5, axis=1)

print(f"Cleaned data: {len(df)} leads")
df.to_csv('cleaned_leads.csv', index=False)
