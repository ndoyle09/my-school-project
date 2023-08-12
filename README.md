# my-school-project

## Goals and TO DO list
### Generating fake data
- [x] Source "fake" school data. 3000 should be OK. Use [faker_education](https://pypi.org/project/faker_education/) since I'm already using [Faker](https://faker.readthedocs.io/en/master/).
 - Per faker_education documentation, "the data was provided for free from the authoritative source https://data-nces.opendata.arcgis.com/ published May 2, 2022."
 - Consider import via API to easily only include records where `school_type` = 'Regular school'.
- [x] Generate fake Project Manager data. 50 should be OK.
- [x] Generate fake Manager data. 6 should be OK.
- [x] Generate fake "team names", one per Manager.
- [x] Randomly "assign" PM to teams. Use an uneven distribution.
- [ ] Randomly "assign" PM to a school. One to one relationship. Use an uneven distribution.
- [ ] Generate a list of "project types". 25 should be OK. 
- [ ] Assign Project Type to School. More than 0 but less than 3 projects for School.
- [x] Generate fake Project data. 5000 to start.
 - Every project should have a `start_date`, and an `end_date`. These should vary between 7 and 13 weeks apart per project.
 - Every project is comprised of 5 milestones that must be completed in order. `Milestone 1` must start after the `start_date` and `Milestone 5` must end before the `end_date`.
 - Every milestone should have a corresponding `due_date` and a `completed_date`. These dates should match most of the time but sometimes should not match. +- 3 days should OK.
 - Every project should start on or after `1-1-2023` and every project should end on or before `12-31-2023`
 - The resulting dataframe and file should contain the following columns: `project_id`, `project_start_date`, `project_end_date`, `milestone_n_due_date`, `milestone_n_completed_date`, where n is milestone 1-5.
- [ ] Create Jupyter Notebook(s) which document code behavior and rationalization.
- [ ] 
      
### Ingest fake data into Postgres
- [ ] Spin up a db with tables to store data.
- [ ] Define constraints
- [ ] Define table relationships

### Build integration into Tableau
- [ ] Create Tableau instance
- [ ] Learn Tableau?

### Tableau Dashboard and Reports
- [ ] Basic styling guide
- [ ] Identify business goals questions, KPIs, metrics.
