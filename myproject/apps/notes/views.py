import logging

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views import generic

from models import Note


logger = logging.getLogger(__name__)


def index_redirect(request):
    return redirect(reverse('notes:index_page'))


class NotesList(generic.ListView):
    template_name = 'notes/notes_index.html'
    context_object_name = 'notes_list'
    model = Note

    def get(self, request, *args, **kwargs):
        try:
            return super(generic.ListView, self).get(request, *args, **kwargs)
        except Exception:
            logger.exception('Exception occurred')

