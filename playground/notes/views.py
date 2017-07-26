from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Note

def index(request):
    note_list = Note.objects.order_by('-pubdate')
    template = loader.get_template('notes/notelist.html')
    context = {
        'note_list': note_list,
    }
    return HttpResponse(template.render(context, request))

def note(request, id):
    return HttpResponse("Dummy Note")