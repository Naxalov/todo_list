from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# example of database

todo = {"task":[]}
def add(request):
	"""this is an api that adds a new task
    ---
    parameters:
            Args:
                    status(bool): True if done, otherwise False
                    taskname(str): The name of the task
                    description(str): The description of the task
    responses:True
            succesfully:
                    {
                            "status": "Ok",
                            "added_task":{
                                    "status": "status" ,
                                    "taskname": "taskname",
                                    "description": "description"
                            }
                    }
    """
	if request.method == 'GET':
		status = request.GET.get('status',False)
		taskname = request.GET.get('taskname',False)
		description = request.GET.get('description',False)
		#---------------------------------------#
		error={'error':[]}
		if not status:
			error['error'].append('Status')
		if not taskname:
			error['error'].append('TaskName')
		if not description:
			error['error'].append('Description')			
#---------------------------------------------------------------------------------------
		if len(error['error'])==0:
			id=len(todo['task'])+1
			add={'id':id,"status":status,"taskname":taskname,"description":description}
			todo['task'].append(add)
			response=add
		else:
			response=error
	return JsonResponse(response)			

def update(request):
	"""this is an api that updates the old function
    parameters:
        Args:
            id(int): New task ID
            taskname(str): The name of the task
            description: The description of the task
        Kwargs:
            status(bool): True if done, otherwise False
    responses:
                error:
                        {
                                "status": "description error."
                        }
        succesfully:
                        {
                                "status": "Ok",
                                "update_task":{
                                        "id": ID,
                                        "status": "status" ,
                                        "taskname": "taskname",
                                        "description": "description"
                                }
                        }
        """

	if request.method=='GET':
		id=request.GET.get('id',False)
		status = request.GET.get('status',False)
		taskname = request.GET.get('taskname',False)
		description = request.GET.get('description',False)
		link_list=todo['task']
#-------------------------------------------------------------#
		id=int(id) 
		leng=len(todo['task'])
		get_valid=[]
		valid=[]
		status=status
		description=description
		taskname=taskname
		if id and leng>=id:
			if status:
				valid.append('status')
				get_valid.append(status)
			if taskname:
				valid.append('taskname')
				get_valid.append(taskname)
			if description:
				valid.append('description')
				get_valid.append(description)
		new_task=[]		
		for index,list1 in enumerate(todo['task']):
			if int(list1['id'])==id:
				for key in valid:
					for new_task in get_valid:
						todo['task'][index][key]=new_task
	return JsonResponse(todo)


def update_status(request):
    """this condition is a variable api
    ---
    parameters:
        Args:
            id(int): New task ID
            status(bool): True if done, otherwise false
        Kwargs:
            taskname(str): The name of the task
            description: The description of the task 
    responses:
      	Error:
			{
				"status": "description error."
			}
        
      	Succesfully:
		  	{
				"status": "Ok",
				"update_task":{
					"id": ID,
					"status": "status" ,
					"taskname": "taskname",
					"description": "description"
				}
			}

    """
    return 0


def get_all(request):
	return JsonResponse(todo)


def remove(request):
	"""this is an api that disables the executed AMA
    ---
    parameters:
        id(int): Task ID
    responses:
      error:
			{
				"status": "description error."
			}
        
      	succesfully:
		  	{
				"status": "Ok",
				"remove_task":{
					"id": ID,
					"status": "status" ,
					"taskname": "taskname",
					"description": "description"
				}
			}
    """
	if request.method=='GET':
		id=request.GET.get('id',False)
		for i,j in enumerate(todo['task']):
			if j['id']==int(id):
				res=todo['task'][i]
				todo['task'].remove(todo['task'][i])
				break
				
				
		if not id:
			response={'status':"id ERROR"}
		else:
			response={'status':'OK',"remove_task":res}
				
		Response=response
		
	return JsonResponse(Response)

def clean_all(request):
	todo['task'].clear()
	return JsonResponse(todo)
