import pandas as pd
import random
from teams import alt_team_names
from faker import Faker

fake = Faker()
Faker.seed(0)

# Define number of Project Managers
numProjectMgrs = 50

# Generate PM names
pm_first_names = [fake.unique.first_name() for _ in range(numProjectMgrs)]
pm_last_names = [fake.unique.last_name() for _ in range(numProjectMgrs)]

names_dict = {'pm_first_name': pm_first_names, 'pm_last_name': pm_last_names}
pm_names = pd.DataFrame(names_dict)

# Randomly assign PMs to a Project Team
pm_names['team_name'] = random.choices(list(alt_team_names.keys()), k=numProjectMgrs)

# Assign corresponding team's nickname based on Project Team number
pm_names['alt_team_name'] = pm_names['team_name'].map(alt_team_names)

# Save DataFrame to CSV
pm_names.to_csv('data/pm_names.csv')
print("Dataset generated and saved as 'data/pm_names.csv'")
