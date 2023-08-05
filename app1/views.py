from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app1.models import *


class Trainerslist(ListView):
    model=Trainer
    template_name='Trainerslist.html'
    context_object_name='tl'
    #queryset=Trainer.objects.filter(trainer_name='sunitha')
    ordering=['trainer_name']
