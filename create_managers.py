import pandas as pd
from teams import alt_team_names
from faker import Faker

fake = Faker()
Faker.seed(0)


# Define number of Project Managers
numManagers = 6

# Generate PM names
mgr_first_names = [fake.unique.first_name() for _ in range(numManagers)]
mgr_last_names = [fake.unique.last_name() for _ in range(numManagers)]

names_dict = {'mgr_first_name': mgr_first_names, 'mgr_last_name': mgr_last_names}
mgr_names = pd.DataFrame(names_dict)

# Assign Manager to a Project Team
mgr_names['team_name'] = list(alt_team_names.keys())

# Assign corresponding team's nickname based on Project Team number
mgr_names['alt_team_name'] = mgr_names['team_name'].map(alt_team_names)

# Save DataFrame to CSV
mgr_names.to_csv('data/mgr_names.csv')
print("Dataset generated and saved as 'data/mgr_names.csv'")
