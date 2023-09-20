import pandas as pd
import random
from faker import Faker
from faker_education import SchoolProvider
from teams import team_names

fake = Faker()
fake.add_provider(SchoolProvider)

Faker.seed(0)


# Generate 100 school objects

def source_schools(num):
    # Source School Objects. Delete school and level.
    schools = pd.DataFrame([fake.school_object() for _ in range(num)])
    schools.drop(['level', 'school'], inplace=True, axis=1)

    # Randomly assign Schools to a Project Team
    schools['team_name'] = random.choices(list(team_names.keys()), k=num, weights=(33, 20, 15, 15, 10, 7))

    # Properly case the District Name
    schools['district'] = schools['district'].str.title()

    # Save DataFrame to CSV
    schools.to_csv('data/Schools.csv')
    print("Dataset generated and saved as 'data/Schools.csv'")


def source_pm_names(num):
    # Generate PM names
    pm_first_names = [fake.unique.first_name() for _ in range(num)]
    pm_last_names = [fake.unique.last_name() for _ in range(num)]

    pm_names = pd.DataFrame(list(zip(pm_first_names, pm_last_names)),
                                 columns=['pm_first_names', 'pm_last_names'])

    # Randomly assign PMs to a Project Team
    pm_names['team_name'] = random.choices(list(team_names.values()), k=num, weights=(33, 20, 15, 15, 10, 7))

    # Assign corresponding team's nickname based on Project Team number
    # pm_names['alt_team_name'] = pm_names['team_name'].map(team_names)

    # Save DataFrame to CSV
    pm_names.to_csv('data/Project_Managers.csv')
    print("Dataset generated and saved as 'data/Project_Managers.csv'")


def source_mgr_names(num):
    # Generate PM names
    mgr_first_names = [fake.unique.first_name() for _ in range(num)]
    mgr_last_names = [fake.unique.last_name() for _ in range(num)]

    mgr_names = pd.DataFrame(list(zip(mgr_first_names, mgr_last_names)),
                             columns=['mgr_first_name', 'mgr_last_name']).reset_index()

    # Assign Manager to a Project Team
    mgr_names['team_name'] = list(team_names.values())

    # Assign corresponding team's nickname based on Project Team number
    # mgr_names['alt_team_name'] = mgr_names['team_name'].map(team_names)

    # Save DataFrame to CSV
    mgr_names.to_csv('data/Managers.csv')
    print("Dataset generated and saved as 'data/Managers.csv'")
