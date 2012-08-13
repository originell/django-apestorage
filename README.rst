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

If you are sick of apes, you might want to check out _django-dogstorage_.

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


.. _placeape.com: http://placeape.com/
__ placeape.com_

