from django.db import models


class Note(models.Model):
    body_text = models.TextField()
    # left for future needs: fancier notes
    label = models.CharField(max_length=100, blank=True)
    # left for future needs: ability to sort notes by date
    creation_date = models.DateTimeField(blank=True, null=True)
