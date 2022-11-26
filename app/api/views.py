from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse


def add(request: WSGIRequest, *args, **kwargs):

    favorite = request.GET.get('a')
    request.user.favorites.add(favorite)
    response_data = {
        'answer': 'success'
    }
    response = JsonResponse(response_data)
    response.status_code = 200
    return response


def remove(request: WSGIRequest, *args, **kwargs):

    favorite = request.GET.get('a')
    request.user.favorites.remove(favorite)
    response_data = {
        'answer': 'success'
    }
    response = JsonResponse(response_data)
    response.status_code = 200
    return response
