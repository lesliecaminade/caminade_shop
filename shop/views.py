from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from . import models
from . import forms
from django.utils import timezone

from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

import requests
from .standard_email import send_email

class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

class IndexView(ListView):
    model = models.Item

class ItemCreateView(CreateView, AdminStaffRequiredMixin):
    model = models.Item
    fields = ['name', 'description','main_image', 'price', 'stock']

    #modify the createview to create a thumbnail while saving the files
    def form_valid(self, form):

        #the thumbnail code

        self.object = form.save()
        self.object.create_thumbnail()

        #inheritance code(do not modify)
        return super().form_valid(form)

class ItemDetailView(DetailView):
    model = models.Item

class ItemDeleteView(DeleteView, AdminStaffRequiredMixin):
    model = models.Item
    success_url = reverse_lazy('shop:item_list')

class ItemUpdateView(UpdateView, AdminStaffRequiredMixin):
    model = models.Item
    fields = ['name', 'description', 'main_image', 'price', 'stock']

    #modify the createview to create a thumbnail while saving the files
    def form_valid(self, form):

        #the thumbnail code

        self.object = form.save()
        self.object.create_thumbnail()

        #inheritance code(do not modify)
        return super().form_valid(form)

# Create your views here.
class OrderRequest(CreateView):
    model = models.Customer
    fields = '__all__'

    def form_valid(self, form):
        SECRET_KEY = '6Lfh4r0ZAAAAAGcQz-3_OUkWr2kOgOXVk7zigK3v'
        recaptcha_response = self.request.POST.get('g-recaptcha-response') #get ggoogle recapthcha response from form
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = {
            'secret': SECRET_KEY,
            'response': recaptcha_response,
        })

        r = r.json()
        if r['success'] == 'false':
            return render(self.request, 'shop/failed.html')
            pass
        else:

            self.object = form.save()
            self.object.send()


        #inheritance code(do not modify)
        return super().form_valid(form)
