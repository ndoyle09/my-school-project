teams = {
    1: 'Luminary',
    2: 'Apex',
    3: 'Genesis',
    4: 'Odyssey',
    5: 'Endeavor',
    6: 'Horizon'
}

from faker import Faker
from faker_education import SchoolProvider
import pandas as pd
import random
from datetime import datetime, timedelta
from teams import team_names

# Initialize Faker and random seed
fake = Faker()
random.seed(42)
fake.add_provider(SchoolProvider)


def create_project_data(num):

    data = []
    for project_id in range(1, num+1):
        project_start_date = fake.date_between_dates(date_start=datetime(2023, 1, 1), date_end=datetime(2023, 12, 11))
        project_end_date = project_start_date + timedelta(weeks=random.randint(7, 13))

        for milestone in range(1, 6):
            due_date = fake.date_between_dates(date_start=project_start_date, date_end=project_end_date)
            completed_date = due_date + timedelta(days=random.randint(-3, 3))

            data.append([project_id, project_start_date, project_end_date, milestone, due_date, completed_date])

    # Create DataFrame
    columns = ['project_id', 'project_start_date', 'project_end_date',
               'milestone', 'due_date', 'completed_date']
    df_projects = pd.DataFrame(data, columns=columns)

    # Create a unique column name for each milestone
    df_projects['milestone'] = df_projects['milestone'].astype(str)
    projects = df_projects.set_index(['project_id', 'project_start_date', 'project_end_date', 'milestone']).unstack()

    # Flatten MultiIndex columns
    projects.columns = [f'{col[1]}_{col[0]}' for col in projects.columns]


    # Reset the index
    projects.reset_index(inplace=True)

    # Create a unique column name for each milestone
    df_projects['milestone'] = 'milestone_' + df_projects['milestone'].astype(str)
    projects = df_projects.set_index(['project_id',
                               'project_start_date',
                               'project_end_date',
                               'milestone']).unstack()


    # Flatten MultiIndex columns
    projects.columns = [f'{col[1]}_{col[0]}' for col in projects.columns]

    # Reset the index
    projects.reset_index(inplace=True)

    # Replace
    case_numbers = [fake.unique.random_int(min=10000000, max=99999999) for row in range(num)]
    projects['project_id'] = case_numbers

    # Assign a team
    projects['team_name'] = random.choices(list(team_names.values()), k=num, weights=(33, 20, 15, 15, 10, 7))

    projects['school_object'] = [fake.school_object() for _ in range(len(projects))]

    projects['school'] = projects['school_object'].apply(lambda x: x['school'])
    projects['district'] = projects['school_object'].apply(lambda x: x['district'])

    projects = projects.drop(columns=['school_object'])

    # projects.to_csv('scratch.csv')

    print(projects)

create_project_data(50)
