import os
import xmlrpclib
import jinja2
from flask import Flask,render_template, request,json

app = Flask(__name__)

@app.route('/getProjects')
def getProjects():
    # gets details for projects i.e. 'In Progress'.  all if blank or filter to a status. you need to pass state=open to see inprogress project

    username = 'admin' #the user
    pwd = 'a'      #the password of the user
    dbname = 'odoo'    #the database
    state = request.args.get('state')
    res = None
    project_details= []

    sock_common = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
    uid = sock_common.login(dbname, username, pwd)
    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')

    if state:
        project_ids = sock.execute(dbname, uid, pwd, 'project.project', 'search', [('state', '=', 'open')])
    else:
        project_ids = sock.execute(dbname, uid, pwd, 'project.project', 'search', [])
    
    if project_ids:
        project_details = sock.execute(dbname, uid, pwd, 'project.project', 'read', project_ids , ['name', 'planned_hours'])
        res = 1
    else:
        res = 0

    return json.dumps({"result":res, "data":project_details})

@app.route('/getProjectTasks')
def getProjectTasks():
    # gets task detail for the nominated project
    username = 'admin' #the user
    pwd = 'a'      #the password of the user
    dbname = 'odoo'    #the database
    project_id = request.args.get('project_id')
    res = None

    sock_common = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
    uid = sock_common.login(dbname, username, pwd)
    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')

    project_details = []
    if not project_id:
        res = 0
    else:
        res = 1
        project_ids = sock.execute(dbname, uid, pwd, 'project.task', 'search', [('project_id', '=', int(project_id) )])
        for project_id in project_ids:
            project_details.append(sock.execute(dbname, uid, pwd, 'project.task', 'read', project_id , ['name', 'planned_hours']))

    return json.dumps({"result":res, "data":project_details})
        

@app.route('/updateProject')
def updateProject():
	# updates 1 or more fields of project i.e. startDate or name. It is any odoo project.project field.
    username = 'admin' #the user
    pwd = 'a'      #the password of the user
    dbname = 'odoo'    #the database
    project_id = request.args.get('project_id')
    datas = request.args.get('data')
    project_details = []
    res = None

    sock_common = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
    uid = sock_common.login(dbname, username, pwd)
    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')

    if project_id and datas:
        datas = json.loads(datas)
        project_details = sock.execute(dbname, uid, pwd, 'project.project', 'write', int(project_id) , datas)
        res = 1
    else:
        res = 0

    return json.dumps({"result":res, "data":project_details})

@app.route('/updateProjectTask')
def updateProjectTask():
	# updates 1 or more fields of project's task i.e. startDate or name. It is any odoo project.project field.

    username = 'admin' #the user
    pwd = 'a'      #the password of the user
    dbname = 'odoo'    #the database
    task_id = request.args.get('task_id')
    datas = request.args.get('data')
    res = None
    project_details = []

    sock_common = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
    uid = sock_common.login(dbname, username, pwd)
    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')

    if task_id and datas:
        datas = json.loads(datas)
        project_details = sock.execute(dbname, uid, pwd, 'project.task', 'write', int(task_id) , datas)
        res = 1
    else:
        res = 0

    return json.dumps({"result":res, "data":project_details})


@app.route('/getProjectTasksForEmployee')
def getProjectTasksForEmployee():
	#get all Tasks for matching employee_id and include project id & name in result.

    username = 'admin' #the user
    pwd = 'a'      #the password of the user
    dbname = 'odoos'    #the database
    employee_id = request.args.get('employee_id')
    res = None
    project_details = []

    sock_common = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
    uid = sock_common.login(dbname, username, pwd)
    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')

    if not employee_id:
        res = 0
    else:
        project_ids = sock.execute(dbname, uid, pwd, 'project.task', 'search', [('user_id', '=', int(employee_id))])
        task_details = sock.execute(dbname, uid, pwd, 'project.task', 'read', project_ids , ['project_id', 'name', 'planned_hours'])
        res = 1
    
    return json.dumps({"result":res, "data":task_details})


if __name__=="__main__":
    app.run()
