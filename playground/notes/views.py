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

def note(request, id):
    template = loader.get_template('notes/detail.html')
    try:
        note = Note.objects.get(pk=id)
        if (request.method == "POST"):
            note.delete()   
            return redirect('..')
        context = {
            'note': note
        }
    except Note.DoesNotExist as e:
        context = {
            'error_message': "This note does not exist!" 
        }
    return HttpResponse(template.render(context, request))

def edit(request, id):
    template = loader.get_template('notes/add.html')
    if (request.method == "POST"):
        form = post_note(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.pk = id
            note.pubdate = timezone.now()
            note.save()
            return redirect('..')
        else:
            context = {
                'error_message': "There's something wrong with your note. It's probably too long!"
            }
    else:
        note = Note.objects.get(pk=id)
        editForm = post_note(initial={'title': note.title , 'text': note.text , 'color': note.color})
        context = {
            'note': editForm
        }
    return HttpResponse(template.render(context, request))