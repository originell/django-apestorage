import tempfile
import urllib2

from django.core.cache import cache
from django.core.files import File
from django.core.files.storage import FileSystemStorage

from apestorage.settings import APE_SIZE


class GreyApe(FileSystemStorage):
    """
    If a file is not found on disk, return a greyscale ape picture.
    """
    def _open(self, name, mode='rb'):
        if not self.exists(name):
            apez = cache.get('apez', False)
            if not apez:
                # Grab a ape from placeape.
                # /g/ means grayscale
                response = urllib2.urlopen('http://placeape.com/g/%s/%s'
                                           % (APE_SIZE[0], APE_SIZE[1]))
                ape_img = response.read()
                cache.set('apez', ape_img)
                ape = tempfile.TemporaryFile()
                ape.write(ape_img)
                # .write places the readhead at the end. Resetting it
                # to the start, otherwise an empty File() will be created.
                ape.seek(0)
                return File(ape)
            else:
                past_ape = tempfile.TemporaryFile()
                past_ape.write(apez)
                past_ape.seek(0)
                return File(past_ape)
        return super(GreyApe, self)._open(name, mode)
