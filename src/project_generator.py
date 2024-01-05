from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

# Initialize Faker and random seed
fake = Faker()
Faker.seed(0)
random.seed(0)

# Define project types with weights for assignment.
project_types = {
    'New Student Registration': 4150,
    'Returning Student Registration': 3050,
    'Registration': 2225,
    'Application': 1350,
    'Intent to Return': 425,
    'Inquiry': 425,
    'New Student Enrollment': 325,
    'Pre-Registration': 275,
    'Enrollment': 225,
    'Information Update': 275,
    'Application for Admission': 150,
    'Returning Student Enrollment': 125,
    'Student Registration': 100,
    'Re-enrollment': 100,
    'Enrollment Contract': 75,
    'New Student Application': 75,
    'New Student Pre-Registration': 75,
    'Lottery Application': 75,
    'Re-Registration': 50,
    'Annual Update': 50,
    'Student Information Update': 50,
    'Bio Update': 50,
    'Annual Student Update': 50,
    'Returning Student Update': 50,
    'Transfer Application': 50
}


def generate_projects(schools_df):
    project_data = []

    for i, row in schools_df.iterrows():
        nces_id = row['nces_id']
        project_count = row['project_count']

        for j in range(project_count):
            project_id = fake.unique.random_int(min=10000000, max=99999999)

            # Generate a random start date
            project_start_date = fake.date_this_year(before_today=True, after_today=True)
            project_end_date = project_start_date + timedelta(weeks=random.randint(7, 13))

            # Generate five dates
            milestone_dates = [project_start_date]
            for milestone in range(4):
                new_date = milestone_dates[-1] + timedelta(days=random.randint(5,15))
                milestone_dates.append(new_date)

            # Sort dates in order
            milestone_dates.sort()

            # Make sure date5 is before project_end_date
            while milestone_dates[-1] >= project_end_date:
                milestone_dates[-1] = milestone_dates[-1] - timedelta(days=random.randint(5,10))

            # Assign dates to variables
            date_1, date_2, date_3, date_4, date_5 = milestone_dates

            # print("Date 1:", date_1.strftime("%Y-%m-%d"))
            # print("Date 2:", date_2.strftime("%Y-%m-%d"))
            # print("Date 3:", date_3.strftime("%Y-%m-%d"))
            # print("Date 4:", date_4.strftime("%Y-%m-%d"))
            # print("Date 5:", date_5.strftime("%Y-%m-%d"))

            project_type = random.choices(list(project_types.keys()), weights=list(project_types.values()), k=1)[0]

            project_data.append({'nces_id': nces_id,
                                 'project_id': project_id,
                                 'project_type': project_type,
                                 'project_start_date': project_start_date,
                                 'project_end_date': project_end_date,
                                 'milestone1': date_1,
                                 'milestone2': date_2,
                                 'milestone3': date_3,
                                 'milestone4': date_4,
                                 'milestone5': date_5
                                 # 'valid_dates': str(project_start_date <= date_1 <= date_2 <= date_3 <= date_4 <= date_5 <= project_end_date),
                                 # 'date1_lt_date2': str(date_1 <= date_2),
                                 # 'date2_lt_date3': str(date_2 <= date_3),
                                 # 'date3_lt_date4': str(date_3 <= date_4),
                                 # 'date4_lt_date5': str(date_4 <= date_5),
                                 # 'date5_lt_end_date': str(date_5 <= project_end_date)
                                 })

    project_data = pd.DataFrame(project_data)

    try:
        project_data.to_csv('data/Projects.csv', index=False)
        print("Dataset generated and saved as 'data/Projects.csv'")
    except PermissionError:
        print("PermissionError: Dataset not saved! Do you have Projects.csv open or lack permission to write?")
    except Exception as e:
        print(f"An error occurred: {e}")
    print(f"Projects generated: {len(project_data)}")
    return project_data
