#! /bin/bash

clear

rm *.pdf

python /home/joao/Programming/presentationplotlib/gen_slides.py \
    \
sld_0.py    \
sld_1.py    \

pdfunite *.pdf presentation_full.pdf

rm page_*

exit 0
