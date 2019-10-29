presentationplotlib
===================

.. image:: https://img.shields.io/static/v1.svg?label=version&message=0.1.0&color=9cf
    

This is an experimental project where I use `matplotlib`_ to create PDF based scientific presentations.

If you want to create PPT presentations with Python please see other libraries like `python-pptx`_.

Installation
------------

Install using::

    python setup.py develop

Compatibilities
~~~~~~~~~~~~~~~

- python==3.7.*

How to run
----------

Preparing slides
~~~~~~~~~~~~~~~~

Use the `slide_example.py` template file to create your slides.

Slides scripts should be defined as a function :code:`slide(page_number, figure=None, ax=None)` and decorated with the template of your choice.

Templates are defined as modules inside the `templates`_ folder. Currently available templates:

- template1

Currently, there is only one template: that of my presentations `¬¬` - `Template1` inside [templates.py](https://github.com/joaomcteixeira/presentationplotlib/blob/master/templates.py). Templates are classes with all kind of attributes and methods that define the template behaviour.  

Prepare a `slide_WHATEVER.py` file for each slide.

You can generate a PDF file for each slide running the _slide_ script independently or, instead, generate a series of slides using `gen_slides.py`, which is useful to insert page numbers in slides (depending on the template).

```
python gen_slides.py slide1.py slide2.py slide3.py ETC...
```

This will generate a PDF file for each slide passed.

Use the program of your choice to concatenate those PDFs. Normally, I generate the full presentation with the help of a *bash* [script](https://github.com/joaomcteixeira/presentationplotlib/blob/master/make_slides.sh) and [pdfunite](http://www.manpagez.com/man/1/pdfunite/) which comes natively with my Linux distribution ([Xubuntu](https://xubuntu.org/) here `:-)`).

.. _matplotlib: https://matplotlib.org/
.. _python-pptx: https://python-pptx.readthedocs.io/en/latest/index.html
