from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import generic

from models import Note


def index_redirect(request):
    return redirect(reverse('notes:index_page'))


class NotesList(generic.ListView):
    template_name = 'notes/notes_index.html'
    context_object_name = 'notes_list'
    model = Note
