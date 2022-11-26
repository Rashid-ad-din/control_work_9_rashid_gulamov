from django.urls import path

from api.views import add

urlpatterns = [
    path('add/', add, name='add'),
    # path('remove/', subtract, name='subtract'),
]
