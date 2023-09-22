import pandas as pd
from src.data_generator import team_names

managers = pd.read_csv('../data/Managers.csv')
pms = pd.read_csv('../data/Project_Managers.csv')
projects = pd.read_csv('../data/Projects.csv')
schools = pd.read_csv('../data/schools.csv')

stats = pd.DataFrame(schools.groupby('team_name').nces_id.count().reset_index())
stats = pd.concat()
print(stats)