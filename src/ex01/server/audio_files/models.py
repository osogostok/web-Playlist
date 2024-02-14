from django.db import models
import mimetypes


class AudioFile(models.Model):
    def __init__(self, name):
        self.name_file = name
        self.content_type = mimetypes.guess_type(self.name_file)[0]

    def __str__(self):
        return self.name_file
