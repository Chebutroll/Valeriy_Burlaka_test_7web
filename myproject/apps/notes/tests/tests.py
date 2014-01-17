from django.test import TestCase
from django.core.urlresolvers import reverse


class NotesViewsTestCase(TestCase):
    fixtures = ['notes_views_testdata.json']

    def test_index_redirect(self):
        response = self.client.get('/')
        self.assertRedirects(response, reverse('notes:index_page'))

    def test_index_page(self):
        response = self.client.get(reverse('notes:index_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('notes_list' in response.context)
        self.assertEqual(len(response.context['notes_list']), 5)
        self.assertTemplateUsed(response, 'notes/notes_base.html')
        self.assertTemplateUsed(response, 'notes/notes_index.html')
        note_1 = response.context['notes_list'][0]
        self.assertEqual(note_1.body_text, 'This is a text for text note')