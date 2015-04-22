1. We are using FLASK framework. So first you need to install Flask into your system.
    sudo pip install Flask

2. you need to start script from terminal. e.g. python app.py

3. We have scripting for ODOO. so ODOO must be started. If not than start it first.

4. In script you need to replace your odoo database name, user, pass, server IP etc.


e.g.
	1.	getProjects (optional Status) - all if blank or filter to a status
	•	gets details for projects i.e. “In Progress"
    CURL command :- 1. Getting all projects =  curl 'http://127.0.0.1:5000/getProjects'
                    2. Getting In Progress projects =  curl 'http://127.0.0.1:5000/getProjects?state="open"'

	2.	getProjectTasks (project_id)
	•	gets task detail for the nominated project
	CURL command :- curl 'http://127.0.0.1:5000/getProjectTasks?project_id=2'
    
    3.	updateProject (id)
	•	updates 1 or more fields (see note 3)  i.e. startDate or name. It is any odoo project.project field
    CURL command :- curl -G -d 'data={"name":"test2","date_start":"04/14/2015"}'  'http://127.0.0.1:5000/updateProject?project_id=7'

	4.	updateProjectTask (id)
	•	updates 1 or more fields (see note 3) i.e. startDate or name. It is any odoo project.project field
    CURL command :- curl -G -d 'data={"name":"Useablityreview","date_start":"04/07/2015"}'  'http://127.0.0.1:5000/updateProjectTask?task_id=21'

	5.	getProjectTasksForEmployee (employee_id)
	•	get all Tasks for matching employee_id
	•	include project id & name in result
    CURL command :- curl 'http://127.0.0.1:5000/getProjectTasksForEmployee?employee_id=1'

