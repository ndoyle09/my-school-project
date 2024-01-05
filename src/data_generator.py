import pandas as pd
import random
from faker import Faker
from faker_education import SchoolProvider
import numpy as np

Faker.seed(55)
fake = Faker()
fake.add_provider(SchoolProvider)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 10)

# Define teams list with weights for PM and District assignment. weights: 33, 20, 15, 15, 10, 7
team_names = {
    'Luminary': 33,
    'Apex': 20,
    'Genesis': 15,
    'Odyssey': 15,
    'Endeavor': 10,
    'Horizon': 7
}
max_managers_per_team = 12
min_managers_per_team = 10
max_districts_per_manager = 10

def generate_school_districts(num_districts):

    # Source School Objects. Delete school and level.
    schools = pd.DataFrame([fake.school_object() for _ in range(num_districts)])
    schools.reset_index(drop=True, inplace=True)
    schools.drop(['level', 'school'], inplace=True, axis=1)
    # Properly case the District Name
    schools['district'] = schools['district'].str.title()

    # Randomly assign Schools to a Project Team
    schools['team_name'] = random.choices(list(team_names.keys()),
                                          k=num_districts,
                                          weights=(list(team_names.values())))
    # Assign random project count
    schools['project_count'] = schools.apply(lambda x: random.randint(1,3), axis=1)

    print(f"\nSchools dataframe: \n"
          f" {schools.head(20)}")

    # Figuring out PM generation
    team_assignments = {}
    for team in team_names:
        # unique_project_managers = [(fake.unique.name_nonbinary()) for _ in range(10)]
        unique_project_managers = [(fake.unique.first_name() + " " + fake.unique.last_name()) for _ in range(10)]
        team_assignments[team] = unique_project_managers
        # print(unique_project_managers)

    teams_df = pd.DataFrame(team_assignments)

    print(f"\nteams_df dataframe: \n"
          f" {teams_df}")

    def get_random_manager_assignment(row):
        team_name = row['team_name']
        column_values = teams_df[team_name]
        return random.choice(column_values)

    schools['assigned_manager'] = schools.apply(get_random_manager_assignment, axis=1)

    print(f"\nmerged results: \n {schools}")
    # # Save DataFrame to CSV
    try:
        schools.to_csv('data/Schools.csv', index=False)
        print("Dataset generated and saved as 'data/Schools.csv'")
    except PermissionError:
        print("PermissionError: Dataset not saved! Do you have project_data.csv open or lack permission to write?")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Return
    return schools

def generate_project_managers(num_managers):
    # Generate PM names
    pm_first_names = [fake.unique.first_name() for _ in range(num_managers)]
    pm_last_names = [fake.unique.last_name() for _ in range(num_managers)]

    pm_names = pd.DataFrame(list(zip(pm_first_names, pm_last_names)),
                            columns=['pm_first_names', 'pm_last_names'])

    # Randomly assign PMs to a Project Team
    pm_names['team_name'] = random.choices(list(team_names.keys()),
                                           k=num_managers,
                                           weights=(list(team_names.values()))
                                           )
    # # Save DataFrame to CSV
    try:
        pm_names.to_csv('data/Project_Managers.csv')
        print("Dataset generated and saved as 'data/Project_Managers.csv'")
    except PermissionError:
        print("PermissionError: Dataset not saved! Do you have project_data.csv open or lack permission to write?")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Return
    return pm_names


def generate_supervisors(num_supervisors):

    # Generate PM names
    supervisor_first_names = [fake.unique.first_name() for _ in range(num_supervisors)]
    supervisor_last_names = [fake.unique.last_name() for _ in range(num_supervisors)]

    supervisor_names = (pd.DataFrame(list(zip(supervisor_first_names, supervisor_last_names)),
                                     columns=['mgr_first_name', 'mgr_last_name'])
                        .reset_index())

    # Assign Manager to a Project Team
    supervisor_names['team_name'] = list(team_names.keys())

    # Save DataFrame to CSV
    try:
        supervisor_names.to_csv('data/Supervisors.csv')
        print("Dataset generated and saved as 'data/Supervisors.csv'")
    except PermissionError:
        print("PermissionError: Dataset not saved! Do you have project_data.csv open or lack permission to write?")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Return
    return supervisor_names

