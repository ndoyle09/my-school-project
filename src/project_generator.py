from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
from data_generator import generate_school_districts

# Initialize Faker and random seed
fake = Faker()
Faker.seed(0)
random.seed(0)

schools_df = generate_school_districts(15)
print(schools_df)

def generate_projects(schools_df):
    project_data = []
    for i, row in schools_df.iterrows():
        nces_id = row['nces_id']
        project_count = row['project_count']

        for j in range(project_count):
            project_id = fake.unique.random_int(min=10000000, max=99999999)
            project_start_date = fake.date_between_dates(date_start=datetime(2023, 1, 1),
                                                         date_end=datetime(2023, 12, 11))
            project_end_date = project_start_date + timedelta(weeks=random.randint(7, 13))

            # Blank list to store milestone data
            milestones_data = []
            for milestone in range(1,6):
                due_date = fake.date_between_dates(date_start=project_start_date, date_end=project_end_date)
                completed_date = due_date + timedelta(days=random.randint(-3, 3))

                milestones_data.append({
                    f"milestone_{milestone}_due_date" : due_date,
                    f"milestone_{milestone}_completed_date": completed_date
                })

            project_data.append({'nces_id':nces_id,
                                 'project_id': project_id,
                                 'project_start_date': project_start_date,
                                 'project_end_date': project_end_date,
                                 'milestones': milestones_data
                                 })
    project_df = pd.DataFrame(project_data)

    project_df = project_df.explode('milestones').reset_index(drop=True)
    project_df = project_df.join(project_df['milestones'].apply(pd.Series))
    project_df.drop(columns='milestones', inplace=True)

    return project_df

    # print(project_data)

project_df = generate_projects(schools_df)
project_df.to_csv('../data/project_df.csv', index=False)