import pandas as pd

managers = pd.read_csv('data/Managers.csv')
pms = pd.read_csv('data/Project_Managers.csv')
projects = pd.read_csv('data/Projects.csv')
schools = pd.read_csv('data/Schools.csv')

print(schools.groupby('team_name').nces_id.count().reset_index())