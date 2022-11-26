from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from webapp.forms.photos import PhotosForm
from webapp.models import Photos


class PhotoView(DetailView):
    template_name = 'photo.html'
    model = Photos
    context_object_name = 'photo'

    # def get(self, request, *args, **kwargs):
    #     favorite = request.GET.get('favorite')
    #     if favorite:
    #         request.user.favorites.add(favorite)
    #     return super().get(request, *args, **kwargs)


class PhotosView(ListView):
    template_name = '../templates/index.html'
    model = Photos


class PostCreateView(CreateView):
    template_name = 'photo_create.html'
    form_class = PhotosForm
    model = Photos

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.save()
            return redirect('photo', pk=photo.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class PostUpdateView(UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotosForm
    model = Photos
    context_object_name = 'photo'

    # def get_success_url(self):
    #     return reverse('profile', kwargs={'upk': self.request.user.pk, 'pk': self.object.pk})

    def get_success_url(self):
        return reverse('index')
