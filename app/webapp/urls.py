from django.urls import path

from webapp.views.photos import PhotosView, PhotoView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PhotosView.as_view(), name='index'),
    path('photos/<int:pk>/', PhotoView.as_view(), name='photo'),
    path('photos/create', PostCreateView.as_view(), name='photo_create'),
    path('photos/<int:pk>/update/', PostUpdateView.as_view(), name='photo_update'),
]
