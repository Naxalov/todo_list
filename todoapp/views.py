from django.shortcuts import render
from django.http import JsonResponse

todo = {"task":[]}

def add(request):
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
		#---------------------------------------------------------------------------------------#
		if len(error['error'])==0:
			add={"status":status,"taskname":taskname,"description":description}
			todo['task'].append(add)
			response=add
		else:
			response=error
	return JsonResponse(response)			

def update(request):
    """this is an api that updates the old function
    ---
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
	
    return 0 


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
    return 0

def clean_all(request):
	todo['task'].clear()
	return JsonResponse(todo)
