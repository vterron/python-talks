#SHELL := /bin/bash

NOTEBOOK_FILE=python-heaps-ters.ipynb
NBCONVERT_OPTS=--SlidesExporter.reveal_transition=none

# Find out the module we need for the HTTP server, depending on the Python
# version. [Source: https://stackoverflow.com/a/4933395]
PYTHON_VERSION_FULL := $(wordlist 2,4,$(subst ., ,$(shell python --version 2>&1)))
PYTHON_VERSION_MAJOR := $(word 1,${PYTHON_VERSION_FULL})
MODULE.PYTHON.2 := SimpleHTTPServer
MODULE.PYTHON.3 := http.server

.PHONY: all slides present clean

all : slides

slides: ${NOTEBOOK_FILE}
	jupyter nbconvert ${NOTEBOOK_FILE} --to slides ${NBCONVERT_OPTS}

present: slides
	python -m ${MODULE.PYTHON.${PYTHON_VERSION_MAJOR}} 8000

clean:
	rm -fv *.{html}
