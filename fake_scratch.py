import pandas as pd
import random

df = pd.read_csv('projectTypes.csv')

choices = []
for choice in range(100):
    choices.append(random.choices(df['Form Name'], weights=df['Counts']))

choices = pd.DataFrame(choices, columns=['form_type'])

project_type_counts = choices['form_type'].value_counts()

print(project_type_counts)