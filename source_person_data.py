import pandas as pd
import random
from faker import Faker
from faker_education import SchoolProvider
fake = Faker()
fake.add_provider(SchoolProvider)


Faker.seed(0)

alt_team_names = {
    1: 'Luminary',
    2: 'Apex',
    3: 'Genesis',
    4: 'Odyssey',
    5: 'Endeavor',
    6: 'Horizon'
}

# Generate 100 school objects
def source_schools(num):
    # Source School Objects. Delete school and level.
    schools = pd.DataFrame([fake.school_object() for _ in range(num)])
    schools.drop(['level', 'school'], inplace=True, axis=1)

    # Randomly assign Schools to a Project Team
    schools['team_assignment'] = random.choices(list(alt_team_names.keys()), k=num)

    # Properly case the District Name
    schools['district'] = schools['district'].str.title()

    # Save DataFrame to CSV
    schools.to_csv('data/schools.csv')
    print("Dataset generated and saved as 'data/schools.csv'")


def source_pm_names(num):
    # Generate PM names
    pm_first_names = [fake.unique.first_name() for _ in range(num)]
    pm_last_names = [fake.unique.last_name() for _ in range(num)]

    names_dict = {
        'pm_first_name': pm_first_names,
        'pm_last_name': pm_last_names
    }
    pm_names = pd.DataFrame(names_dict)

    # Randomly assign PMs to a Project Team
    pm_names['team_name'] = random.choices(list(alt_team_names.keys()), k=num)

    # Assign corresponding team's nickname based on Project Team number
    pm_names['alt_team_name'] = pm_names['team_name'].map(alt_team_names)

    # Save DataFrame to CSV
    pm_names.to_csv('data/pm_names.csv')
    print("Dataset generated and saved as 'data/pm_names.csv'")


def source_mgr_names(num):
    # Generate PM names
    mgr_first_names = [fake.unique.first_name() for _ in range(num)]
    mgr_last_names = [fake.unique.last_name() for _ in range(num)]

    names_dict = {
        'mgr_first_name': mgr_first_names,
        'mgr_last_name': mgr_last_names
    }
    mgr_names = pd.DataFrame(names_dict)

    # Assign Manager to a Project Team
    mgr_names['team_name'] = list(alt_team_names.keys())

    # Assign corresponding team's nickname based on Project Team number
    mgr_names['alt_team_name'] = mgr_names['team_name'].map(alt_team_names)

    # Save DataFrame to CSV
    mgr_names.to_csv('data/mgr_names.csv')
    print("Dataset generated and saved as 'data/mgr_names.csv'")
