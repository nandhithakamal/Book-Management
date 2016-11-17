from django.shortcuts import render
from .models import book
from django.views import generic
from django.views.generic.edit import CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import Context


class index(generic.ListView):
    template_name= 'app/main_page.html'
    context_object_name= 'p'
    
    def get_queryset(self):
        return book.objects.all()

class result(generic.ListView):
    template_name='app/result.html'
    context_object_name='r'
    
    def get_queryset(self):
        return book.objects.all()


class Insert(CreateView):
    model = book
    fields = ['title','author','edition','totalpages']


#class Delete(DeleteView):

#    model = book
#    success_url = reverse_lazy('book:index')
    
    
    
class details(generic.DetailView):
    model = book
    template_name = 'app/details.html'
    context_object_name = 'p'

    def get_queryset(self):
        return book.objects.all()