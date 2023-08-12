# my-school-project

## Goals and TO DO list

- [x] Source "fake" school data. 3000 should be OK.
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
