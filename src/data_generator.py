import pandas as pd
import random
from faker import Faker
from faker_education import SchoolProvider

fake = Faker()
fake.add_provider(SchoolProvider)
Faker.seed(0)

pd.set_option('display.max_columns', None)

# Define teams list with weights for PM and District assignment. weights: 33, 20, 15, 15, 10, 7
team_names = {
    'Luminary': 33,
    'Apex': 20,
    'Genesis': 15,
    'Odyssey': 15,
    'Endeavor': 10,
    'Horizon': 7
}

num_districts = 50
num_managers = 50

# Generate num_districts of School objects
def generate_school_districts(num_districts):
    # Source School Objects. Delete school and level.
    schools_df = pd.DataFrame([fake.school_object() for _ in range(num_districts)])
    schools_df.drop(['level', 'school'], inplace=True, axis=1)

    # Randomly assign Schools to a Project Team
    schools_df['team_name'] = random.choices(list(team_names.keys()),
                                          k=num_districts,
                                          weights=(list(team_names.values()))
                                             )

    # Properly case the District Name
    schools_df['district'] = schools_df['district'].str.title()
    print("\n 'schools_df' dataset generated")

    # Assign random project count
    schools_df['project_count'] = schools_df.apply(
        lambda x: random.randint(1,3), axis=1
    )

    # Return
    return schools_df

    # # Save DataFrame to CSV
    # schools.to_csv('data/Schools.csv')
    # print("Dataset generated and saved as 'data/Schools.csv'")

def generate_project_managers(num_managers):
    # Generate PM names
    pm_first_names = [fake.unique.first_name() for _ in range(num_managers)]
    pm_last_names = [fake.unique.last_name() for _ in range(num_managers)]

    pm_names = pd.DataFrame(list(zip(pm_first_names, pm_last_names)),
                                 columns=['pm_first_names', 'pm_last_names'])

    # Randomly assign PMs to a Project Team
    pm_names['team_name'] = random.choices(list(team_names.values()),
                                           k=num_managers,
                                           weights=(list(team_names.values()))
                                           )
    # Return
    return pm_names
    print("pm_names dataset generated")

    # # Save DataFrame to CSV
    # pm_names.to_csv('data/Project_Managers.csv')
    # print("Dataset generated and saved as 'data/Project_Managers.csv'")


def generate_supervisors(num_supervisors):
    # Generate PM names
    supervisor_first_names = [fake.unique.first_name() for _ in range(num_supervisors)]
    supervisor_last_names = [fake.unique.last_name() for _ in range(num_supervisors)]

    supervisor_names = (pd.DataFrame(list(zip(supervisor_first_names, supervisor_last_names)),
                             columns=['mgr_first_name', 'mgr_last_name'])
                 .reset_index())

    # Assign Manager to a Project Team
    supervisor_names['team_name'] = list(team_names.values())

    # Return
    return supervisor_names
    print("supervisor_names dataset generated")

    # # Save DataFrame to CSV
    # mgr_names.to_csv('data/Managers.csv')
    # print("Dataset generated and saved as 'data/Managers.csv'")


print(generate_school_districts(20))