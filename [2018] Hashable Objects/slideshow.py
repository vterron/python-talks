#! /usr/bin/env python3

# Author: Victor Terron (c) 2019
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

"""Use nbconvert as a library to convert a notebook to slides.

Equivalent to...

NBCONVERT_OPTS=--SlidesExporter.reveal_transition=none \
   	           --reveal-prefix=https://cdn.jsdelivr.net/reveal.js/3.0
jupyter nbconvert ${NOTEBOOK_FILE} --to slides ${NBCONVERT_OPTS}

... plus the ability of generating an alternative version of the slides via
the --alternative flag. For more information, refer to the docstring of the
AlternativeSlidesExporter class in this module.

"""

import argparse
import copy
import os.path

import nbconvert.exporters
import nbconvert.preprocessors
import nbformat
import traitlets
import traitlets.config


class AlternativeSlidesExporter(nbconvert.exporters.SlidesExporter):
    """A nbconvert exporter to generate an alternative version of slides.

    This nbconvert exporter subclasses SlidesExporter to add additional
    functionality: the ability to use the same notebook to generate two
    different versions of the presentation: (a) the regular one and (b)
    the alternative one.

    This is achieved via cell tags, which must start with "alternative:"
    and follow with the value that overrides the slideshow's "slide_type"
    when the alternative version is generated.

    For example...

    [...]
    "metadata": {
     "slideshow": {
      "slide_type": "skip"
     },
     "tags": [
      "alternative:subslide"
     ]
    },
    [...]

    ... means that the slide is normally skipped ("slide_type": "skip"),
    but rendered as a subslide (because of the "alternative:subslide" tag)
    when the alternative version is generated.

    You may also use this functionality to get the opposite effect: a
    slide that is by default rendered but that, via the "alternative:skip"
    tag, is skipped when the alternative version is generated.
    """

    alternative_edition = traitlets.Bool(
        help="Generate the alternative version of the slides",
        default_value=False).tag(config=True)

    def prepare(self, nb):
        if not self.alternative_edition:
            return nb
        nb = copy.deepcopy(nb)
        for index, cell in enumerate(nb.cells):
            self.prepare_cell(cell, index)
        return nb

    @staticmethod
    def prepare_cell(cell, index):
        tags = [t for t in cell.metadata.get('tags', []) if t.startswith("alternative:")]

        if not tags:
            return
        if len(tags) > 1:
            raise ValueError("Multiple alternative:* tags in cell (index={})".format(index))
        if tags:
            _, slide_type = tags.pop().split(":")
            print('Rendering alternative slide (index={}) with type={}'.format(index, slide_type))
            cell.metadata.slideshow.slide_type = slide_type

    def from_notebook_node(self, nb, **kwargs):
        nb = self.prepare(nb)
        return super().from_notebook_node(nb, **kwargs)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("notebook")
    parser.add_argument(
        "-a", "--alternative",
        action="store_true",
        help="Generate the alternative version of the slides")
    args = parser.parse_args()

    with open(args.notebook) as fd:
        contents = fd.read()

    c = traitlets.config.Config()
    c.AlternativeSlidesExporter.reveal_transition = 'none'
    c.AlternativeSlidesExporter.reveal_url_prefix = 'https://cdn.jsdelivr.net/reveal.js/3.0'
    c.AlternativeSlidesExporter.alternative_edition = args.alternative
    exporter = AlternativeSlidesExporter(config=c)
    notebook = nbformat.reads(contents, as_version=4)
    body, _ = exporter.from_notebook_node(notebook)

    slides_path = os.path.splitext(args.notebook)[0] + '.slides.html'
    with open(slides_path, 'wt') as fd:
        fd.write(body)
