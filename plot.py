import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Database Connection
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'health_data'
DB_USER = 'postgres'
DB_PASSWORD = 'pokemon'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

query = "SELECT * FROM healthcare_data LIMIT 100"
df = pd.read_sql(query, engine)

bins = [0, 18, 35, 50, 65, 100]
labels = ['0-18', '19-35', '36-50', '51-65', '65+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

age_group_counts = df.groupby('age_group')['name'].count().reset_index().rename(columns={'name': 'patient_count'})

plt.figure(figsize=(8, 5))
sns.barplot(x='age_group', y='patient_count', data=age_group_counts, palette='coolwarm')
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.title("Patient Count by Age Group (Limited to 1000 Records)")
plt.show()