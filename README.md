# presentationplotlib

This is an experimental project of me using [matplotlib](https://matplotlib.org/) to create PDF based presentations.

If you want real PPT presentations please see the [python-pptx](https://python-pptx.readthedocs.io/en/latest/index.html). But, because all my presentations are PDF based, I want to find my way with matplotlib :-)

# How to run

Use the `slide_example.py` template file to create your slides. Slide configuration should be defined as a function `slide(page_number, figure=None, ax=None)` and decorated with the template of your choice. Currently, there is only one template: that of my presentations. Prepare a `slide_WHATEVER.py` for each slide.

You can generate a PDF file for each slide running the _slide_ script independently or, instead, generate a series of slides using `gen_slides.py`, which is useful to insert page numbers in slides (depending on the template).

```
python gen_slides.py slide1.py slide2.py slide3.py ETC...
```

This will generate a PDF file for each slide passed. Use the program of your choice to concatenate those PDFs.
