from django.utils import timezone
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Note
from .add_note import post_note

def index(request):
    note_list = Note.objects.order_by('-pubdate')
    template = loader.get_template('notes/notelist.html')
    context = {
        'note_list': note_list
    }
    return HttpResponse(template.render(context, request))

def note(request, id):
    return HttpResponse("Dummy Note")

def add(request):
    template = loader.get_template('notes/add.html')
    if (request.method == "POST"):
        form = post_note(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.pubdate = timezone.now()
            note.save()
            return redirect('..')
    else:
        note = post_note()
        context = {
            'note': note
        }
    return HttpResponse(template.render(context, request))