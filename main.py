from src import data_generator
from src import project_generator


def main():
    data_generator.generate_project_managers(50)
    data_generator.generate_school_districts(500)
    data_generator.generate_supervisors(6)
    project_generator.generate_projects(500)

if __name__ == '__main__':
    main()

