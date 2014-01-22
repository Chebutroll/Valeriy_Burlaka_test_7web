from django.template import Template, Context
from django.utils.unittest import TestCase

from factories import NotesFactory


class TestNotesTags(TestCase):

    def render_note_test(self, note_id, expected_out):
        t = Template("{{% load notes_tags %}}{{% render_note {note_id} %}}".format(note_id=note_id))
        c = Context()
        out = t.render(c)
        self.assertEqual(expected_out, out)

    def test_render_existing_note(self):
        NotesFactory(body_text='body text for fancy note')
        expected_out = u'<p><span class="note_body">body text for fancy note</span></p>'
        self.render_note_test(1, expected_out)

    def test_render_non_existing_note(self):
        expected_out = u'<p><span class="note_body"></span></p>'
        self.render_note_test(2, expected_out)
