====================
django-apestorage
====================
apestorage is a so called *development storage engine*.

Many people have the problem with gigantomanic production databases with 
gigabytes of pictures/files. It is a pain to keep the image files synchronised 
between development and production environments. 

Therefore I have written this storage engine. In case a file is not found, 
an image from placeape.com_ will be used/displayed
instead.

If you are sick of apes, you might want to check out django-dogstorage_ or django-kittenstorage_.

sorl-thumbnail users
====================

Note that newer versions of sorl-thumbnail have an integrated dummy engine, which
can load images from various dummy sources. This is super cool and I highly recommend
this over dogstorage. Go and have a look at THUMBNAIL_DUMMY_.

The setting for placeholder apes source would be:

    ``THUMBNAIL_DUMMY_SOURCE = http://placeape.com/%(width)s/%(height)s``

or if you prefer grayscale:

    ``THUMBNAIL_DUMMY_SOURCE = http://placeape.com/g/%(width)s/%(height)s``

Setup
=====
It's on pypi.

    ``pip install django-apestorage``

Feel free to clone from github too. Forking is welcome as well :-)

In your django settings file:

    ``DEFAULT_FILE_STORAGE = 'apestorage.storages.GreyApe'``

Storage Engines
===============
apestorage offers two engines:

1. ``apestorage.storages.GreyApe``
2. ``apestorage.storages.ColorApe``

Choose depending on the saturation you want. I prefer ``GreyApe`` since it
does have a pretty classy look.

Settings
========
There is only one setting:

APE_SIZE  
    Default: ``(1024, 1024)``

    A tuple of format `(width, height)`, specifiying the size of the image 
    requested from placeape__.

.. _django-kittenstorage: https://github.com/originell/django-kittenstorage/
.. _django-dogstorage: https://github.com/originell/django-dogstorage/
.. _THUMBNAIL_DUMMY: http://sorl-thumbnail.readthedocs.org/en/latest/reference/settings.html#thumbnail-dummy
.. _placeape.com: http://placeape.com/
__ placeape.com_

