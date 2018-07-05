from django.views import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .form import UserForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login'
    redirect_field_name = '/'
    template_name = 'music/index.html' 
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    # It is the blue print u use for ur form
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # Display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
        
    # process form data    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            #user.password = 'chicken_and_run' we can't write the pw like this bcause of the hash code
            #proper way :
            user.set_password(password)
            user.save()

            # How to auth and log to the user
            # return User objects if credentials are correct
            # authenticate : check if the u and the pk are in db
            user = authenticate(username=username, password=password)
            if user is not None :
                if user.is_active :
                    #how to log in : just like that
                    login(request, user)
                    # refer to them
                    #request.user.username ...
                    return redirect('music:index')
                else :
                    return logout(request) 

        return render(request, self.template_name, {'form': form})  




