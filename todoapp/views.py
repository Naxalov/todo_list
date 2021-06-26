from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def add(request):

    """
        The add function adds task to list

        Argument:
                request
        
        Returns:
                your response(JsonResponse)

    
    """


    return JsonResponse({"key":"value"})


def update(request):
    return 0


def update_status(request):
    return 0


def get_all(request):
    return 0


def remove(request):
    return 0


