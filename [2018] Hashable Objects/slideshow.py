#! /usr/bin/env python3

# Author: Victor Terron (c) 2019
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

"""Use nbconvert as a library to convert a notebook to slides.

Equivalent to:

NBCONVERT_OPTS=--SlidesExporter.reveal_transition=none \
   	           --reveal-prefix=https://cdn.jsdelivr.net/reveal.js/3.0
jupyter nbconvert ${NOTEBOOK_FILE} --to slides ${NBCONVERT_OPTS}

"""

import nbconvert.exporters
import nbformat
import os.path
import sys
import traitlets.config

if __name__ == "__main__":

    notebook_path = sys.argv[1]
    with open(notebook_path) as fd:
        contents = fd.read()

    c = traitlets.config.Config()
    c.SlidesExporter.reveal_transition="none"
    c.SlidesExporter.reveal_url_prefix="https://cdn.jsdelivr.net/reveal.js/3.0"
    exporter = nbconvert.exporters.SlidesExporter(config=c)

    notebook = nbformat.reads(contents, as_version=4)
    body, _ = exporter.from_notebook_node(notebook)

    slides_path = os.path.splitext(notebook_path)[0] + ".slides.html"
    with open(slides_path, "wt") as fd:
        fd.write(body)
