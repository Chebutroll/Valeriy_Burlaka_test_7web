from django import template
from django.core.exceptions import ObjectDoesNotExist

from ..models import Note


register = template.Library()

@register.inclusion_tag('notes/note_inclusion.html')
def render_note(note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except ObjectDoesNotExist:
        note = None
    return {'note': note}