from django_webtest import WebTest
from django.core.urlresolvers import reverse

from factories import NotesFactory


class TestNotesViews(WebTest):

    def test_index_redirect(self):
        response = self.app.get(reverse('index_redirect'))
        self.assertRedirects(response, reverse('notes:index_page'))

    def test_index_page(self):
        NotesFactory()
        NotesFactory(body_text='This is a text for text note')
        response = self.client.get(reverse('notes:index_page'))
        self.assertTrue('notes_list' in response.context)
        self.assertEqual(len(response.context['notes_list']), 2)
        self.assertTemplateUsed(response, 'notes/notes_base.html')
        self.assertTemplateUsed(response, 'notes/notes_index.html')
        note_1 = response.context['notes_list'][1]
        self.assertEqual(note_1.body_text, 'This is a text for text note')
