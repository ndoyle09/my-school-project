import source_person_data
import create_project_data

def main():
    source_person_data.source_pm_names(50)
    source_person_data.source_schools(500)
    source_person_data.source_mgr_names(6)
    create_project_data.create_project_data(1)

if __name__ == '__main__':
    main()
