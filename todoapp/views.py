from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# example of database
todo = {}
def add(request):

    """this is an api that adds a new task
    ---
    parameters:
        Args:
            id(int): New task ID
            status(bool): True if done, otherwise False
            taskname(str): The name of the task
            description(str): The description of the task 
    responses:
        400:
          JsonResponse:{'result':'Error!'} 
        500:     
          JsonResponse:{'checking':'don't input : id,taskname,status or description'}
        200:
          JsonResponse:{'result': 'succesfully!'}


    """
    return JsonResponse({})




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
        400:
          JsonResponse:{
          'result':'Error!'
                          }
        500: 
          JsonResponse:{
          'checking':'don't input : id,taskname or description'
                      }
        200:
          JsonResponse:{'result': 'succesfully!'}
              


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
      400:
        JsonResponse:{'result':'Error!'} 
      500:       
        JsonResponse:{'checking':'don't input : id or status'}
      200:
        JsonResponse:{'result': 'succesfully!'}


    """
    return 0


def get_all(request):
    """this is the api that gives all ADH
    ---
    parameters:
        None
    responses:
      400:
        JsonResponse:{'result':'Error!'} 
      200:
        
        JsonResponse:{'result':'ok',
                        [
                            {
                            'id':ID,
                             'status':status,
                             'task_name':task_name,
                             'description':description
                             },
                             ......

                             ......

                        ]
    """
    return 0


def remove(request):
    """this is an api that disables the executed AMA
    ---
    parameters:
        id(int): Task ID
    responses:
      400:
        JsonResponse:{ 'result ':'Error!'} 
      500:     
        JsonResponse:{'checking':'don't input : id '}
      200:
        JsonResponse:{'result': 'succesfully!'}

    """
    return 0

def clean_all(request):
	"""
	This method clears all added tasks
	"""
	return 0
