from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


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


    """
    return 0




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


    """
    return 0


def get_all(request):
    """this is the api that gives all ADH
    ---
    parameters:
        None
    responses:


    """
    return 0


def remove(request):
    """this is an api that disables the executed AMA
    ---
    parameters:
        id(int): Task ID
    responses:

    """
    return 0


