from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    print(request.method)
    print(request.headers)
    if request.method == "POST":
        print('POST')
        print(request.POST)
    data = {'a':5}
    return JsonResponse(data)