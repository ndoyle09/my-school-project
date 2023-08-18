import pandas as pd
import random
from faker import Faker
from faker_education import SchoolProvider
from teams import alt_team_names

fake = Faker()

fake.add_provider(SchoolProvider)
Faker.seed(0)

# Define number of Schools
numSchools = 500

# Source School Objects. Delete school and level.
schools = pd.DataFrame([fake.school_object() for _ in range(numSchools)])
schools.drop(['level','school'], inplace=True, axis=1)

# Randomly assign Schools to a Project Team
schools['team_assignment'] = random.choices(list(alt_team_names.keys()), k=numSchools)

# Properly case the District Name
schools['district'] = schools['district'].str.title()

# Save DataFrame to CSV
schools.to_csv('data/schools.csv')
print("Dataset generated and saved as 'data/schools.csv'")


