import factory

from ..models import Note


class NotesFactory(factory.DjangoModelFactory):

    FACTORY_FOR = Note

    body_text = 'Blank note'
    label = None
    creation_date = None