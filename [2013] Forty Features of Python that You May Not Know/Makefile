# Inspired by Stephan Bourduas's LaTeX Makefile:
# http://www.iml.ece.mcgill.ca/~stephan/node/13

SHELL := /bin/bash

PDFLATEX=pdflatex
PDFLATEX_OPTS=-interaction=nonstopmode -halt-on-error

BASENAME=forty-features
TEX_FILE=${BASENAME}.tex
PDF_FILE=${BASENAME}.pdf

.PHONY: all pdf clean

all : pdf cover

cover: pdf
	pdf2svg $(PDF_FILE) pics/cover.svg

pdf: $(TEX_FILE)
	$(PDFLATEX) $(PDFLATEX_OPTS) $(TEX_FILE)
	$(PDFLATEX) $(PDFLATEX_OPTS) $(TEX_FILE)

clean:
	rm -fv *.{aux,log,nav,out,snm,toc,vrb}
