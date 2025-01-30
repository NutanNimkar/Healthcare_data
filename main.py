import pandas as pd

df = pd.read_csv('healthcare_dataset 2.csv')

df.columns = df.columns.str.lower().str.replace(" ", "_")

# Clean and normalize text fields
df['name'] = df['name'].str.title().str.strip()
df['hospital'] = df['hospital'].str.title().str.strip()
df['doctor'] = df['doctor'].str.title().str.strip()

# Handle missing and invalid values
df['billing_amount'] = df['billing_amount'].fillna(0).round(2)
df['date_of_admission'] = pd.to_datetime(df['date_of_admission'], errors='coerce')
df['discharge_date'] = pd.to_datetime(df['discharge_date'], errors='coerce')

# Remove duplicate records (keeping unique visits)
df.drop_duplicates(subset=['name', 'date_of_admission', 'hospital'], inplace=True)
df.dropna(inplace=True)

billing_per_hospital = df.groupby('hospital')['billing_amount'].sum().reset_index()
billing_per_hospital = billing_per_hospital[billing_per_hospital['billing_amount'] >= 0]
billing_per_hospital = billing_per_hospital.sort_values(by='billing_amount', ascending=False)

admissions_count = df.groupby('hospital')['name'].count().reset_index().rename(columns={'name': 'total_admissions'})

df['length_of_stay'] = (df['discharge_date'] - df['date_of_admission']).dt.days
df = df[df['length_of_stay'] >= 0]  # Remove invalid stays

avg_stay_by_admission = df.groupby('admission_type')['length_of_stay'].mean().round(0).astype(int).reset_index()

bins = [0, 18, 35, 50, 65, 100]
labels = ['0-18', '19-35', '36-50', '51-65', '65+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

age_group_counts = df.groupby('age_group')['name'].count().reset_index()

output_csv_file = "cleaned_healthcare_data.csv"
df.to_csv(output_csv_file, index=False)

print("Total Billing Per Hospital:\n", billing_per_hospital)
print("\nAdmissions Count by Hospital:\n", admissions_count)
print("\nAverage Stay Duration by Admission Type:\n", avg_stay_by_admission)
print("\nPatients by Age Group:\n", age_group_counts)
