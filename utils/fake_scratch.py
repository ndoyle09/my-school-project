from faker import Faker
from datetime import datetime, timedelta
import random
from pprint import pprint
fake = Faker()

project_types = {
    'New Student Registration': 4150,
    'Returning Student Registration': 3050,
    'Registration': 2225,
    'Application': 1350,
    'Intent to Return': 425,
    'Inquiry': 425,
    'New Student Enrollment': 325,
    'Pre-Registration': 275,
    'Enrollment': 225,
    'Information Update': 275,
    'Application for Admission': 150,
    'Returning Student Enrollment': 125,
    'Student Registration': 100,
    'Re-enrollment': 100,
    'Enrollment Contract': 75,
    'New Student Application': 75,
    'New Student Pre-Registration': 75,
    'Lottery Application': 75,
    'Re-Registration': 50,
    'Annual Update': 50,
    'Student Information Update': 50,
    'Bio Update': 50,
    'Annual Student Update': 50,
    'Returning Student Update': 50,
    'Transfer Application': 50
}

def generate_fake_project():
    project_name = random.choices(list(project_types.keys()), weights=list(project_types.values()), k=1)[0]
    start_date = fake.date_this_decade()
    end_date = start_date + timedelta(days=random.randint(30, 365))

    tasks = []
    for i in range(5):
        task_name = "Milestone " + str(i+1)
        task_start_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        task_end_date = task_start_date + timedelta(days=random.randint(1, max(1, (end_date - task_start_date).days)))

        tasks.append({
            'task_name': task_name,
            'task_start_date': task_start_date,
            'task_end_date': task_end_date.fromisoformat
        })

    return {
        'project_name': project_name,
        'start_date': start_date,
        'end_date': end_date,
        'tasks': tasks
    }

fake_projects = [generate_fake_project() for _ in range(50)]
# Print the first project for testing
pprint(fake_projects)

# Save the data to a file (optional)
# Example: save to a JSON file
import json

# with open('fake_projects.json', 'w') as file:
#     json.dump(fake_projects, file, indent=2)
