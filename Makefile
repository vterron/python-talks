# Inspired by Stephan Bourduas's LaTeX Makefile:
# http://www.iml.ece.mcgill.ca/~stephan/node/13

SHELL := /bin/bash

PDFLATEX=pdflatex
PDFLATEX_OPTS=-interaction=nonstopmode -halt-on-error

TEX_FILE=python-cuarenta.tex

.PHONY: all pdf clean

all : pdf

pdf: $(TEX_FILE)
	$(PDFLATEX) $(PDFLATEX_OPTS) $(TEX_FILE)
	$(PDFLATEX) $(PDFLATEX_OPTS) $(TEX_FILE)

clean:
	rm -fv *.{aux,log,nav,out,snm,toc}
