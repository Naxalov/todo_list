from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def add(request):

    """this is an api that adds a new task
    ---
    parameters:
        id: int
        status: bool
        taskname: str
        description: str
    responses:
      500:
        JsonResponse:{"result":"Error!"} 
        JsonResponse:{"checking":"don't input : id,taskname,status or description"}
      200:
        JsonResponse:{"result": "succesfully!"}
        

    """
    return 0




def update(request):
    """this is an api that updates the old function
    ---
    parameters:
        id: int
        status: bool
        taskname: str
        description: str
    responses:
      500:
        JsonResponse:{"result":"Error!"} 
        JsonResponse:{"checking":"don't input : id,taskname,status or description"}
      200:
        JsonResponse:{"result": "succesfully!"}

    """
    return 0


def update_status(request):
    """this condition is a variable api
    ---
    parameters:
        id: int
        status: bool
    responses:
      500:
        JsonResponse:{"result":"Error!"} 
        JsonResponse:{"checking":"don't input : id or status"}
      200:
        JsonResponse:{"result": "succesfully!"}

    """
    return 0


def get_all(request):
    """this is the api that gives all ADH
    ---
    parameters:
        no
    responses:
      500:
        JsonResponse:{"result":"Error!"} 
      200:
        
        JsonResponse:{"key":"value",
                      ......
                      ......
                      }

    """
    return 0


def remove(request):
    """this is an api that disables the executed AMA
    ---
    parameters:
        id: int
    responses:
      500:
        JsonResponse:{"result":"Error!"} 
        JsonResponse:{"checking":"don't input : id "}
      200:
        JsonResponse:{"result": "succesfully!"}

    """
    return 0


