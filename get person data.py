from faker import Faker
from faker_education import SchoolProvider
fake = Faker()
fake.add_provider(SchoolProvider)
import pandas as pd
import random

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
    schools = pd.DataFrame(
        [fake.school_object() for _ in range(num)]
    )
    schools['team_assignment'] = random.choices(list(alt_team_names.keys()), k=num)
    print(schools)
    schools.to_json('data/schools.json')

def source_pm_names(num):
    pm_first_names = [fake.unique.first_name() for _ in range(num)]
    pm_last_names = [fake.unique.last_name() for _ in range(num)]
    names_dict = {'pm_first_name': pm_first_names, 'pm_last_name': pm_last_names}
    names = pd.DataFrame(names_dict)
    names['team_name'] = random.choices(list(alt_team_names.keys()), k=num)
    names['alt_team_name'] = [alt_team_names[team] for team in names['team_name']]
    # print(names)
    # print(names.groupby('alt_team_name').alt_team_name.count())
    names.to_csv('data/pm_names.csv')

def source_mgr_names(num):
    pm_first_names = [fake.unique.first_name() for _ in range(num)]
    pm_last_names = [fake.unique.last_name() for _ in range(num)]
    names_dict = {'mgr_first_name': pm_first_names, 'mgr_last_name': pm_last_names}
    names = pd.DataFrame(names_dict)
    names['mgr_email'] = names['mgr_first_name'] + "." + names['mgr_last_name'] + "@sagebrush.com"
    names['team_name'] = list(alt_team_names.keys())
    names['alt_team_name'] = [alt_team_names[team] for team in names['team_name']]
    # names['alt_team_name'] = ['Luminary', 'Apex', 'Genesis', 'Odyssey', 'Endeavor', 'Horizon']
    print(names)
    names.to_csv('data/mgr_names.csv')



source_schools(100)
source_pm_names(50)
source_mgr_names(6)
